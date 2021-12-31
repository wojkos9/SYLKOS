from django.urls import path
from users.api.views import CurrentUserAPIView, CreateCustomUserView, UserGroupsView, UserProjectsView, user_grant_rights

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    path("user/projects", UserProjectsView.as_view(), name="current-user-projects"),
    path("user/groups", UserGroupsView.as_view(), name="current-user-groups"),
    path("user/<int:pk>/grant", user_grant_rights),
    path("create_user/", CreateCustomUserView.as_view())
]
