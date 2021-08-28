from rest_framework import serializers
from django.db import models
from django.db.models import fields
from voting.models import Group, Project, Comment, Voting, VotingType, ImageAlbum, Image


class GroupSerializer(serializers.ModelSerializer):

    count_user = serializers.SerializerMethodField()
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Group
        fields = "__all__"

    def get_count_user(self, instance):
        return instance.members.count()


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class ImageAlbumSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageAlbum
        fields = "__all__"


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"


# class ProjectImageSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = ProjectImage
#         fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    dislikes_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ["voters_like", "voters_dislike"]
        # fields = "__all__"

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
    class Meta:
        model = Voting
        fields = "__all__"
