from django.contrib.auth.models import AbstractUser
from django.db import models
import voting.models as voting_models


class PersonalKey(models.Model):
    value = models.IntegerField(primary_key=True)  # TODO: Change to more reasonable type
    used = models.IntegerField(default=0)


class CustomUser(AbstractUser):
    key = models.ForeignKey(PersonalKey, on_delete=models.DO_NOTHING, null=True)
    groups = models.ManyToManyField(voting_models.Group, related_name="user_groups", blank=True)
    voting_history = models.ManyToManyField(voting_models.Voting, related_name="user_voting_history", blank=True)
