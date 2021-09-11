from voting.models import Voting
from django.urls import path
from voting.api.views import CommentRUDAPIView, GroupListCreateAPIView, GroupDetailAPIView, ProjectListCreateAPIView, ProjectDetailAPIView, JoinGroupAPIView, CommentCreateAPIView, CommentListAPIView, CommentLikeAPIView, CommentDislikeAPIView, VotingTypeView, VotingView, ImageAlbumListCreateAPIView, ImageListCreateAPIView, PhotoListCreateAPIView, PhotoDetailAPIView
from rest_framework.routers import SimpleRouter

voting_router = SimpleRouter()
voting_router.register('voting', VotingView)
voting_router.register('voting_type', VotingTypeView)

urlpatterns = [
    path('groups/', GroupListCreateAPIView.as_view(), name="group-list"),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name="group-detail"),
    path('groups/<int:pk>/member/', JoinGroupAPIView.as_view(), name="group-join"),
    path('projects/', ProjectListCreateAPIView.as_view(), name="project-list"),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name="project-detail"),
    path('projects/<int:pk>/comment/', CommentCreateAPIView.as_view(), name="comment-add"),
    path('projects/<int:pk>/comments/', CommentListAPIView.as_view(), name="comment-list"),
    path('comments/<int:pk>/', CommentRUDAPIView.as_view(), name="comment-ruda"),
    path('comments/<int:pk>/like', CommentLikeAPIView.as_view(), name="comment-like"),
    path('comments/<int:pk>/dislike', CommentDislikeAPIView.as_view(), name="comment-like"),
    path('albums/', ImageAlbumListCreateAPIView.as_view(), name="albums-list"),
    path('images/', ImageListCreateAPIView.as_view(), name="images-list"),
    path('photo/', PhotoListCreateAPIView.as_view(), name="photo-list"),
    path('photo/<int:pk>/', PhotoDetailAPIView.as_view(), name="photo-detail"),
    *voting_router.urls
]