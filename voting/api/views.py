from rest_framework import generics
from voting.models import Group, Project
from voting.api.permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from voting.api.serializers import GroupSerializer, ProjectSerializer
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


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
