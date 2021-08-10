from rest_framework import generics
from voting.models import Group
from voting.api.permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly
from voting.api.serializers import GroupSerializer

class GroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all().order_by("id")
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]

class GroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]

