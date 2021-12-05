from django.db.models.deletion import CASCADE
from users.models import BasicUser
from django.db import models
from django.conf import settings
from django.utils import timezone

class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1500)
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="members", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GroupKey(models.Model):
    group = models.ForeignKey(Group, on_delete=CASCADE)
    value = models.CharField(max_length=20, primary_key=True)
    created = models.DateTimeField(auto_now_add=True)
    handed_over = models.BooleanField(default=False)

class VotingType(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Voting(models.Model):
    name = models.CharField(max_length=200, default='')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    voting_type = models.ForeignKey(VotingType, on_delete=CASCADE)
    group = models.ForeignKey(Group, on_delete=CASCADE)

    def __str__(self):
        if self.name:
            return self.name
        projects_included = Project.objects.filter(voting=self)
        return f"Voting {self.pk} ({', '.join([str(x) for x in projects_included])})"


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    budget = models.DecimalField(decimal_places=2, max_digits=100)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    stage = models.CharField(max_length=50)
    finish_date = models.DateTimeField()
    group = models.ForeignKey(Group, on_delete=CASCADE)
    voting = models.ForeignKey(Voting, on_delete=CASCADE)
    votes = models.BigIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=150, blank=True, default='')
    group = models.ForeignKey(Group, on_delete=CASCADE, null=True)
    project = models.ForeignKey(Project, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.image.url


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name="comments")
    rating = models.FloatField(blank=True)
    voters_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="voters_like")
    voters_dislike = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="voters_dislike")
    project = models.ForeignKey(
        Project, on_delete=CASCADE, related_name="comment")

    def __str__(self):
        return f"{self.author.username}: {self.content[:10]}..."


class Vote(models.Model):
    voting = models.ForeignKey(Voting, on_delete=CASCADE, db_index=True)
    user = models.ForeignKey(BasicUser, on_delete=CASCADE)
    project = models.ForeignKey(Project, on_delete=CASCADE)
    points = models.IntegerField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"v:{self.voting} u:{self.user} p:{self.project} x:{self.points}"
