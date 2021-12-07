from voting.models import Group
from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)

        return request.method in permissions.SAFE_METHODS or is_admin


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.author == request.user

class IsGroupAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        group: Group = Group.objects.filter(pk=view.kwargs.get('pk')).first()
        if not group:
            return False
        return group.admin_users.all().filter(pk=request.user.pk).exists()

    def has_object_permission(self, request, view, group: Group):
        return group.admin_users.filter(pk=request.user.pk).exists()
