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


class VotingType(models.Model):
    name = models.CharField(primary_key=True, max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name


class Voting(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    voting_type = models.ForeignKey(VotingType, on_delete=models.CASCADE)

    def __str__(self):
        projects_included = Project.objects.filter(voting=self)
        return f"Voting {self.pk} ({', '.join([str(x) for x in projects_included])})"


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    budget = models.DecimalField(decimal_places=2, max_digits=100)
    stage = models.CharField(max_length=50)
    finish_date = models.DateTimeField()
    image_path = models.CharField(max_length=200, blank=True) 
    rating = models.FloatField(blank=True, null=True) # wywala mi bez tego jak zostawiam puste to pole przy dodawaniu projektu
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
    rating = models.FloatField(blank=True)
    voters_like = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="voters_like")
    voters_dislike = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="voters_dislike")
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="comment")

    def __str__(self):
        return f"{self.author.username}: {self.content[:10]}..."
