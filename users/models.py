from django.contrib.auth.models import AbstractUser
from django.db import models
from voting.models import Group

class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="user_groups", blank=True)
