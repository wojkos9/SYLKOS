from rest_framework import serializers
from django.db import models
from django.db.models import fields 
from voting.models import Group

class GroupSerializer(serializers.ModelSerializer):
    
    count_user = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = "__all__"

    def get_count_user(self, instance):
        return instance.members.count()



    