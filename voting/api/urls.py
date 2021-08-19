from django.urls import path
from voting.api.views import CommentRUDAPIView, GroupListCreateAPIView, GroupDetailAPIView, ProjectListCreateAPIView, ProjectDetailAPIView, JoinGroupAPIView, CommentCreateAPIView, CommentListAPIView

urlpatterns = [
    path('groups/', GroupListCreateAPIView.as_view(), name="group-list"),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name="group-detail"),
    path('groups/<int:pk>/member/', JoinGroupAPIView.as_view(), name="group-join"),
    path('projects/', ProjectListCreateAPIView.as_view(), name="project-list"),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name="project-detail"),
    path('projects/<int:pk>/comments/', CommentListAPIView.as_view(), name="comment-list"),
    path('projects/<int:pk>/comment/', CommentCreateAPIView.as_view(), name="comment-detail"),
    path('comment/<int:pk>/', CommentRUDAPIView.as_view(), name="comment-ruda"),

]