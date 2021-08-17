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


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    budget = models.DecimalField(decimal_places=2)
    stage = models.CharField(max_length=50)
    finish_date = models.DateTimeField()
    image_path = models.CharField(max_length=200, blank=True)
    rating = models.FloatField(blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
