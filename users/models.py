from django.contrib.auth.models import AbstractUser
from django.db import models
from voting.models import Group, Voting


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name="user_groups", blank=True)
    voting_history = models.ManyToManyField(Voting, related_name="user_voting_history", blank=True)
