from django.db.models.expressions import Value
from django.db.models.query import QuerySet
from rest_framework import serializers
from django.http import request
from django.db import models
from django.db.models import fields, manager
from django.forms.models import model_to_dict
from statistics import mean
from rest_framework.generics import get_object_or_404
from django.db.models import CharField, Value, Count, Avg, Sum
from voting.models import Group, GroupKey, Project, Comment, Voting, VotingType, Photo, Vote

class GroupSerializer(serializers.ModelSerializer):

    count_user = serializers.SerializerMethodField()
    members = serializers.StringRelatedField(many=True)
    images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Group
        fields = "__all__"

    def get_count_user(self, instance):
        return instance.members.count()

    def get_images(self, instance):
        group_images = Photo.objects.filter(group=instance.pk).values()
        if len(group_images) == 0:
            group_images = [{"image" : "no_images/no_picture.png"}]
        return group_images

class GroupKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupKey
        fields = "__all__"

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    rating_avg = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    user_has_commented = serializers.SerializerMethodField()
    user_comment = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = "__all__"

    def get_rating_avg(self, instance):
        sum = 0.0
        comments = Comment.objects.filter(project=instance.pk)

        for comment in comments:
            sum += comment.rating

        if len(comments) > 0:
            return round(((float)(sum / len(comments))), 2)
        return 0.0

    def get_images(self, instance):
        project_images = Photo.objects.filter(project=instance.pk).values()
        if len(project_images) == 0:
            project_images = [{"image" : "no_images/no_picture.png"}]
        return project_images

    def get_user_has_commented(self, instance):
        request = self.context.get("request")
        return instance.comment.filter(author=request.user).exists()

    def get_user_comment(self, instance):
        request = self.context.get("request")
        comment = Comment.objects.filter(project=instance.pk, author=request.user).first()
        return [CommentSerializer(comment, context=self.context).data]

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    user_has_liked = serializers.SerializerMethodField()
    user_has_disliked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ["voters_like", "voters_dislike"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d.%m.%Y %H:%M")

    def get_user_has_liked(self, instance):
        request = self.context.get("request")
        return instance.voters_like.filter(pk=request.user.pk).exists()

    def get_user_has_disliked(self, instance):
        request = self.context.get("request")
        return instance.voters_dislike.filter(pk=request.user.pk).exists()

    def get_likes_count(self, instance):
        return instance.voters_like.count()

    def get_dislikes_count(self, instance):
        return instance.voters_dislike.count()


class VotingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VotingType
        fields = "__all__"


class VotingSerializer(serializers.ModelSerializer):
    projects = serializers.SerializerMethodField(read_only=True)
    users_votes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Voting
        fields = "__all__"

    class Vote(serializers.ModelSerializer):
        class Meta:
            model = Vote
            fields = ("project", "points")

    def get_users_votes(self, instance):
        q = self.context.get('request')
        votes = Vote.objects.filter(voting=instance.pk, user=q.user)

        return [VotingSerializer.Vote(v).data for v in votes]

    def get_projects(self, instance):
        voting_projects = Project.objects.filter(voting=instance.pk).annotate(
            rating_avg=Value('0.0', output_field=CharField())).values()
        voting_projects = voting_projects.annotate(
            images=Value('', output_field=CharField()))
        request = self.context.get("request")

        for idx, proj in enumerate(voting_projects):
            sum = 0.0
            avg = 0.0
            comments = Comment.objects.filter(project=proj['id'])
            project_images = Photo.objects.filter(project=proj['id']).values()
            user_has_commented = Comment.objects.filter(author=request.user, project=proj['id']).exists()
            tmp_user_comment  = Comment.objects.filter(project=instance.pk, author=request.user).first()
            user_comment = [CommentSerializer(tmp_user_comment, context=self.context).data]
            if len(project_images) == 0:
                project_images = [{"image" : "no_images/no_picture.png"}]

            for comment in comments:
                sum += comment.rating

            if len(comments) > 0:
                avg = round(((float)(sum / len(comments))), 2)

            voting_projects[idx]['rating_avg'] = avg
            voting_projects[idx]['images'] = project_images
            voting_projects[idx]['user_has_commented'] = user_has_commented
            voting_projects[idx]['user_comment'] = user_comment

        return voting_projects


from django.db.models import F
class VoteSerializer(serializers.Serializer):
    MAJORITY_VAL = lambda d, _: [len([x for x in d if x==v]) for v in (1, 0)] == [1, len(d)-1]
    APPROVAL_VAL = lambda d, _: all(x in (0,1) for x in d)
    BORDA_VAL = lambda d, t: all(i in d for i in range(t))
    VOTING_VALS = {"majority": MAJORITY_VAL, "approval": APPROVAL_VAL, "borda": BORDA_VAL}
    class InnerVotes(serializers.Serializer):
        project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
        points = serializers.IntegerField()

    voting = serializers.PrimaryKeyRelatedField(queryset=Voting.objects.all())
    choice = InnerVotes(many=True)

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user

        choice = attrs['choice']
        voting: Voting = attrs['voting']

        if any(e['project'].voting.id != voting.id for e in choice):
            raise Exception("Project not in voting")

        if len(set([e['project'].id for e in choice])) != len(choice):
            raise Exception("Duplicate projects")

        data = [x['points'] for x in choice]
        total = Project.objects.filter(voting=voting).count()

        vtype = voting.voting_type.name.lower()
        voting_validator = self.VOTING_VALS[vtype if vtype in self.VOTING_VALS else "majority"]  # TODO: Maybe some warning instead of fallback to majority

        if voting_validator(data, total):
            return attrs
        else:
            raise Exception("Forbidden vote")

    def create(self, validated_data):
        voting = validated_data['voting']
        user = validated_data['user']
        choice = validated_data['choice']

        old_votes: QuerySet[Vote] = Vote.objects.filter(voting=voting, user=user)

        votes_f = F('votes')

        pj = dict()
        for vp in old_votes.select_related('project'):
            p: Project = vp.project
            p.votes = votes_f - vp.points
            pj[p.pk] = p

        for c in choice:
            p: Project = c['project']
            pts = c['points']
            pk = p.pk
            if pk not in pj:
                p.votes = votes_f + pts
                pj[pk] = p
            else:
                pj[pk].votes += pts

        old_votes.delete()
        Project.objects.bulk_update(pj.values(), ['votes'])

        votes = [Vote.objects.create(voting=voting, user=user, **c) for c in choice]
        return votes
