from django.db import models
from django.conf import settings

class Group(models.Model):
    # domyslne ID powinno starczyć?
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=150, blank=True, default='')
    description = models.TextField()
    members_number = models.PositiveIntegerField()
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="members")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name



