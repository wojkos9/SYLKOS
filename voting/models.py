from users.models import BasicUser
from django.db import models
from django.conf import settings


class Photo(models.Model):
    image = models.ImageField(upload_to='images/')


class Group(models.Model):
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=150, blank=True, default='')
    description = models.TextField()
    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="members", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ForeignKey(
        Photo, on_delete=models.CASCADE, null=True, blank=True,  related_name="photo")

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


def get_upload_path(instance, filename):
    model = instance.album.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'{name}/images/{filename}'


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()

    def thumbnails(self):
        return self.images.filter(width__lt=100, length_lt=100)


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    width = models.FloatField(default=100)
    length = models.FloatField(default=100)
    album = models.ForeignKey(
        ImageAlbum, related_name='images', on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    budget = models.DecimalField(decimal_places=2, max_digits=100)
    stage = models.CharField(max_length=50)
    finish_date = models.DateTimeField()
    album = models.OneToOneField(
        ImageAlbum, related_name='model', on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    votes = models.BigIntegerField(default=0)

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


class Vote(models.Model):
    voting = models.ForeignKey(Voting, on_delete=models.CASCADE)
    user = models.ForeignKey(BasicUser, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"v:{self.voting} u:{self.user} p:{self.project} x:{self.points}"
