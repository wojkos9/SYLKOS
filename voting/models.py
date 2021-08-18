from django.db import models
from django.conf import settings


class Group(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=150, blank=True, default='')
    description = models.TextField()
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="members", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    budget = models.DecimalField(decimal_places=2, max_digits=100)
    stage = models.CharField(max_length=50)
    finish_date = models.DateTimeField()
    image_path = models.CharField(max_length=200, blank=True)
    rating = models.FloatField(blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    rating = models.FloatField(blank=True)
    commenters = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="commenters")
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.author.username}: {self.content[:10]}..."
