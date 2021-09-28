from django.contrib import admin
from voting.models import Group, Project, Comment, Vote, VotingType, Voting, ImageAlbum, Image, Photo

admin.site.register(Group)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(VotingType)
admin.site.register(Voting)
admin.site.register(Photo)
admin.site.register(Vote)
