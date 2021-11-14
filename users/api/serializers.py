from django.db.models.query import InstanceCheckMeta
from rest_framework import serializers
from users.models import CustomUser, PersonalKey
from rest_framework.exceptions import ValidationError
from voting.models import Group, Photo

class UserDisplaySerializer(serializers.ModelSerializer):

    groups = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = "__all__"

    def get_groups(self, instance):
        user_groups = Group.objects.filter(members=instance.pk).values()
       
        for idx, group in enumerate(user_groups):
            group_images = Photo.objects.filter(group=group['id']).values()
            if len(group_images) == 0:
                group_images = [{"image" : "images/no_picture.png"}]
            user_groups[idx]['images'] = group_images

        return user_groups

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
