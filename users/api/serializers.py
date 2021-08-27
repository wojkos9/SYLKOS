from rest_framework import serializers
from users.models import CustomUser

class UserDisplaySerializer(serializers.ModelSerializer):

    #user_groups = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ["username", "groups"]
        # fields="__all__"

    #def get_user_groups(self, instance):
