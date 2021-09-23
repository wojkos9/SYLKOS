from rest_framework import serializers
from django.http import request
from django.db import models
from django.db.models import fields, manager
from django.forms.models import model_to_dict
from statistics import mean
import re
from voting.models import Group, Project, Comment, Voting, VotingType, ImageAlbum, Image, Photo, Vote


class GroupSerializer(serializers.ModelSerializer):

    count_user = serializers.SerializerMethodField()
    members = serializers.StringRelatedField(many=True)
    photos = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = "__all__"

    def get_count_user(self, instance):
        return instance.members.count()

    def get_photos(self, instance):
        pattern = re.compile(r"[0-9]+")
        res = pattern.findall(str(instance.image))

        if len(res) > 0:
            res_i = int(res[0])
            images = Photo.objects.filter(id=res_i).values()
            return images

        return []


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    rating_avg = serializers.SerializerMethodField(read_only=True)

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
        return ''


class ImageAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageAlbum
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ["voters_like", "voters_dislike"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d.%m.%Y %H:%M")

    def get_user_has_commented(self, instance):
        request = self.context.get("request")
        return instance.voters_like.filter(pk=request.user.pk).exists()

    def get_likes_count(self, instance):
        return instance.voters_like.count()

    def get_dislikes_count(self, instance):
        return instance.voters_dislike.count()


class VotingTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = VotingType
        fields = "__all__"


class VotingSerializer(serializers.ModelSerializer):
    voted_projects = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Voting
        fields = "__all__"

    def get_voted_projects(self, instance):
        projects = Project.objects.filter(voting=instance.pk).values()

        return projects


class VoteSerializer(serializers.Serializer):
    class InnerVotes(serializers.Serializer):
        project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
        points = serializers.IntegerField()

    voting = serializers.PrimaryKeyRelatedField(queryset=Voting.objects.all())
    choice = InnerVotes(many=True)

    def validate(self, attrs):
        attrs['user'] = self.context['request'].user

        MAJORITY_VOTING_VAL = lambda d: [1, len(d)-1] == [len([x for x in d if x==v]) for v in (1, 0)]

        choice = attrs['choice']

        if any(e['project'].voting.id != attrs['voting'].id for e in choice):
            raise Exception("Project not in voting")

        if len(set([e['project'].id for e in choice])) != len(choice):
            raise Exception("Duplicate projects")

        data = [x['points'] for x in choice]

        d = data
        print([len([x for x in d if x==v]) for v in (1, 0)])

        if MAJORITY_VOTING_VAL(data):
            return attrs
        else:
            raise Exception("Forbidden vote")

    def create(self, validated_data):
        voting=validated_data['voting']
        user = validated_data['user']
        Vote.objects.filter(voting=voting, user=user).delete()
        votes = [Vote.objects.create(voting=voting, user=user, **c)
            for c in validated_data['choice']]
        return votes
