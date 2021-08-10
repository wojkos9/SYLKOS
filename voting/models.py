from django.db import models


class Group(models.Model):
    # domyslne ID powinno starczyć?
    name = models.CharField(max_length=50)
    subname = models.CharField(max_length=150, blank=True, default='')
    description = models.TextField()
    members_number = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



