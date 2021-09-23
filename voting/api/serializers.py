from rest_framework import serializers
from django.http import request
from django.db import models
from django.db.models import fields, manager
from django.forms.models import model_to_dict
from statistics import mean
import re
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
        return ''

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
<<<<<<< HEAD

=======
>>>>>>> b14bc65ac5a9c210205273949014f28315da87ee
    class Meta:
        model = VotingType
        fields = "__all__"


class VotingSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    voted_projects = serializers.SerializerMethodField(read_only=True)

=======
    projects = serializers.SerializerMethodField(read_only=True)
>>>>>>> e43b7490a86a45bcfb1db04dd3db5716819cf6eb
    class Meta:
        model = Voting
        fields = "__all__"

<<<<<<< HEAD
    def get_voted_projects(self, instance):
        projects = Project.objects.filter(voting=instance.pk).values()

        return projects
=======
    def get_projects(self, instance):
            voting_projects = Project.objects.filter(voting=instance.pk).values()
            return voting_projects
>>>>>>> e43b7490a86a45bcfb1db04dd3db5716819cf6eb
