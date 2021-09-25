from django.db.models.expressions import Value
from rest_framework import serializers
from django.http import request
from django.db import models
from django.db.models import fields, manager
from django.forms.models import model_to_dict
from statistics import mean
import re
from django.db.models import CharField, Value, Count, Avg, Sum
from voting.models import Group, Project, Comment, Voting, VotingType, Photo


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
        return group_images


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):

    rating_avg = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)

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
        return project_images


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
    projects = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Voting
        fields = "__all__"

    def get_projects(self, instance):
        voting_projects = Project.objects.filter(voting=instance.pk).annotate(
            rating_avg=Value('0.0', output_field=CharField())).values()
        voting_projects = voting_projects.annotate(
            images=Value('', output_field=CharField()))

        for idx, proj in enumerate(voting_projects):
            sum = 0.0
            avg = 0.0
            comments = Comment.objects.filter(project=proj['id'])
            project_images = Photo.objects.filter(project=proj['id']).values()

            for comment in comments:
                sum += comment.rating

            if len(comments) > 0:
                avg = round(((float)(sum / len(comments))), 2)

            voting_projects[idx]['rating_avg'] = avg
            voting_projects[idx]['images'] = project_images

        return voting_projects
