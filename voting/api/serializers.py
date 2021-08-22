from rest_framework import serializers
from django.db import models
from django.db.models import fields
from voting.models import Group, Project, Comment


class GroupSerializer(serializers.ModelSerializer):

    count_user = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = "__all__"

    def get_count_user(self, instance):
        return instance.members.count()


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    user_has_commented = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = ["project", "voters"]

    def get_created_at(self, instance):
        return instance.created_at.strftime("%d.%m.%Y %H:%M")

    def get_user_has_commented(self, instance):
        request = self.context.get("request")
        return instance.voters.filter(pk=request.user.pk).exists()
