from django.urls import path
from voting.api.views import GroupListCreateAPIView, GroupDetailAPIView

urlpatterns = [
    path('groups/', GroupListCreateAPIView.as_view(), name="group-list"),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name="group-detail"),
]