from django.contrib import admin
from voting.models import Group, Project, Comment

admin.site.register(Group)
admin.site.register(Project)
admin.site.register(Comment)
