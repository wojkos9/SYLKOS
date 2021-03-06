from voting.models import Voting
from django.urls import path
from voting.api.views import CommentRUDAPIView, GroupListCreateAPIView, GroupDetailAPIView, ListGroupKeys, ProjectListCreateAPIView, ProjectDetailAPIView, JoinGroupAPIView, CommentCreateAPIView, CommentListAPIView, CommentLikeAPIView, CommentDislikeAPIView, VotingTypeView, VotingView, PhotoListCreateAPIView, PhotoDetailAPIView
from rest_framework.routers import SimpleRouter
from voting.api import views

voting_router = SimpleRouter()
voting_router.register('voting', VotingView)
voting_router.register('voting_type', VotingTypeView)

urlpatterns = [
    path('groups/', GroupListCreateAPIView.as_view(), name="group-list"),
    path('groups/<int:pk>/', GroupDetailAPIView.as_view(), name="group-detail"),
    path('groups/<int:pk>/member/', JoinGroupAPIView.as_view(), name="group-join"),
    path('groups/<int:pk>/genkeys', views.group_gen_keys, name="group-genkeys"),
    path('groups/<int:pk>/keys', ListGroupKeys.as_view(), name="group-keys"),
    path('projects/', ProjectListCreateAPIView.as_view(), name="project-list"),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name="project-detail"),
    path('projects/<int:pk>/comment/', CommentCreateAPIView.as_view(), name="comment-add"),
    path('projects/<int:pk>/comments/', CommentListAPIView.as_view(), name="comment-list"),
    path('comments/<int:pk>/', CommentRUDAPIView.as_view(), name="comment-ruda"),
    path('comments/<int:pk>/like', CommentLikeAPIView.as_view(), name="comment-like"),
    path('comments/<int:pk>/dislike', CommentDislikeAPIView.as_view(), name="comment-like"),
    path('photo/', PhotoListCreateAPIView.as_view(), name="photo-list"),
    path('photo/<int:pk>/', PhotoDetailAPIView.as_view(), name="photo-detail"),
    path('vote/', views.VoteView.as_view(), name="submit-vote"),
    path('vote/<int:pk>/', views.DeleteVoteView.as_view(), name="delete-vote"),
    path('voting/<int:pk>/timeplot', views.voting_stats, name='voting_timeplot'),
    *voting_router.urls
]