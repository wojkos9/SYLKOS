from rest_framework import serializers
from users.models import CustomUser
from voting.models import Group, Project, Voting

class UserDisplaySerializer(serializers.ModelSerializer):
    user_groups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields="__all__"
