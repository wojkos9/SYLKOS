from voting.api.serializers import GroupSerializer, ProjectSerializer
from rest_framework import serializers
from users.models import CustomUser, PersonalKey
from rest_framework.exceptions import ValidationError


class UserOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("color_mode",)

    def is_valid(self, raise_exception=False):
        if any(k not in self.Meta.fields for k in self.initial_data.keys()):
            if raise_exception:
                raise ValidationError("Unexpected_parameters")
            return False
        return super().is_valid(raise_exception=raise_exception)

class UserDisplaySerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ("password",)

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
