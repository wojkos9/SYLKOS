from django.contrib import admin
from voting.models import Group, Project, Comment, VotingType, Voting, ImageAlbum, Image, Photo

admin.site.register(Group)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(VotingType)
admin.site.register(Voting)
admin.site.register(ImageAlbum)
admin.site.register(Image)
admin.site.register(Photo)
