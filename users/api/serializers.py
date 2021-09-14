from rest_framework import serializers
from users.models import CustomUser, PersonalKey
from rest_framework.exceptions import ValidationError


class UserDisplaySerializer(serializers.ModelSerializer):

    #user_groups = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ["username", "groups"]
        # fields="__all__"

    #def get_user_groups(self, instance):


class CustomUserSerializer(serializers.ModelSerializer):
    key_value = serializers.IntegerField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'key_value']

    def validate(self, attrs):
        super().validate(attrs)

        key = PersonalKey.objects.filter(value=attrs['key_value']).first()

        if not key:
            raise ValidationError("KEY_INVALID")
        elif key.used != 0:
            raise ValidationError("KEY_USED")

        del attrs['key_value']
        return {**attrs, "key": key}

    def create(self, validated_data: dict):
        key: PersonalKey = validated_data.get('key')
        key.used = 1
        key.save()
        return CustomUser.objects.create(**validated_data)
