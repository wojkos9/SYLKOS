from django.db.models.query import InstanceCheckMeta
from rest_framework import serializers
from users.models import CustomUser
from voting.models import Group


class UserDisplaySerializer(serializers.ModelSerializer):

    groups = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = "__all__"

    def get_groups(self, instance):
        user_groups = Group.objects.filter(members=instance.pk).values()

        return user_groups
