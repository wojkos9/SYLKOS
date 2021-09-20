from django.db import models
from voting.models import Voting, Project
from django.db.models.deletion import CASCADE
import users.models as user_models


class Vote(models.Model):
    voting = models.ForeignKey(Voting, on_delete=CASCADE)
    user = models.ForeignKey(user_models.CustomUser, on_delete=CASCADE)
    project = models.ForeignKey(Project, on_delete=CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"v:{self.voting} u:{self.user} p:{self.project} x:{self.points}"
