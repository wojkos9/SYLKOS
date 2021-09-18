from rest_framework import generics
from voting.models import Group, Project, Comment, VotingType, Voting, Photo
from voting.api.permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from voting.api.serializers import CommentSerializer, GroupSerializer, ProjectSerializer, ProjectSerializer, VotingTypeSerializer, VotingSerializer, PhotoSerializer
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated


class GroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all().order_by("id")
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class GroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class PhotoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Photo.objects.all().order_by("id")
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]

class PhotoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticated]


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by("id")
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


# class ProjectImageListCreateAPIView(generics.ListCreateAPIView):
#     queryset = ProjectImage.objects.all().order_by("id")
#     serializer_class = ProjectSerializer
#     permission_classes = [IsAuthenticated]


class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class JoinGroupAPIView(APIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        user = request.user

        group.members.remove(user)
        group.save()

        user.groups.remove(group)
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(group, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        user = request.user

        group.members.add(user)
        group.save()

        user.groups.add(group)
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(group, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user = self.request.user
        pk = self.kwargs.get("pk")
        project = get_object_or_404(Project, pk=pk)

        if project.comment.filter(author=request_user).exists():
            raise ValidationError("You have already commented this Project!")

        serializer.save(author=request_user, project=project)


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Comment.objects.filter(project=pk).order_by("-created_at")


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]


class CommentLikeAPIView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.voters_like.remove(user)
        comment.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.voters_like.add(user)
        comment.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentDislikeAPIView(APIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.voters_dislike.remove(user)
        comment.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        user = request.user

        comment.voters_dislike.add(user)
        comment.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(comment, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)


class VotingTypeView(viewsets.ModelViewSet):
    queryset = VotingType.objects.all()
    serializer_class = VotingTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class VotingView(viewsets.ModelViewSet):
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer


