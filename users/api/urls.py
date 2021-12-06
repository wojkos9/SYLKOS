from django.urls import path
from users.api.views import CurrentUserAPIView, CreateCustomUserView, user_grant_rights

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    path("user/<int:pk>/grant", user_grant_rights),
    path("create_user/", CreateCustomUserView.as_view())
]
