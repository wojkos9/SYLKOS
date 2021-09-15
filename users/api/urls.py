from django.urls import path
from users.api.views import CurrentUserAPIView, CreateCustomUserView

urlpatterns = [
    path("user/", CurrentUserAPIView.as_view(), name="current-user"),
    path("create_user/", CreateCustomUserView.as_view())
]
