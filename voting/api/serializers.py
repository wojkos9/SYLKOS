from rest_framework import serializers
from django.db.models import fields 
from voting.models import Group

class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"

    def countUsers(self, instance):
        return instance.members.count()



    