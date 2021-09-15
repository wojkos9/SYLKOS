from rest_framework import serializers
from django.http import request
from django.db import models
from django.db.models import fields, manager
from django.forms.models import model_to_dict
from statistics import mean
import re
from voting.models import Group, Project, Comment, Voting, VotingType, ImageAlbum, Image, Photo


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
        images_data = []

        images = Photo.objects.all().values()
        images_inner = instance.photos.all().values()
        for i in images:
            for i_i in images_inner:
                if i['id'] == i_i['id']:
                    print(i)
                    images_data.append(i)

        return images_data


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
