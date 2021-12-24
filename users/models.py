from django.contrib.auth.models import AbstractUser
from django.db import models

class PersonalKey(models.Model):
    value = models.IntegerField(primary_key=True)  # TODO: Change to more reasonable type
    used = models.IntegerField(default=0)

class BasicUser(AbstractUser):
    key = models.ForeignKey(PersonalKey, on_delete=models.DO_NOTHING, null=True)

from voting.models import Group, Voting

class CustomUser(BasicUser):
    user_groups = models.ManyToManyField(Group, related_name="user_groups", blank=True)
    voting_history = models.ManyToManyField(Voting, related_name="user_voting_history", blank=True)