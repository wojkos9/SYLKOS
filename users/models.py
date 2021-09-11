from django.contrib.auth.models import AbstractUser
from django.db import models
from voting.models import Group, Voting


class CustomUser(AbstractUser):
    pass
