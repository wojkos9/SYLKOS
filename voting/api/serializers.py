from rest_framework import serializers
from django.db.models import fields 
from voting.models import Group, Project

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"

    def countUsers(self, instance):
        pass

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
    