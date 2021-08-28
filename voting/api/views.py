from rest_framework import generics
from voting.models import Group, Project, Comment, VotingType, Voting
from voting.api.permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from voting.api.serializers import CommentSerializer, GroupSerializer, ProjectSerializer, VotingTypeSerializer, VotingSerializer
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated


class GroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all().order_by("id")
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]


class GroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by("id")
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]


class JoinGroupAPIView(APIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]

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


class VotingTypeView(viewsets.ModelViewSet):
    queryset = VotingType.objects.all()
    serializer_class = VotingTypeSerializer
    permission_classes = [IsAdminOrReadOnly]


class VotingView(viewsets.ModelViewSet):
    queryset = Voting.objects.all()
    serializer_class = VotingSerializer
