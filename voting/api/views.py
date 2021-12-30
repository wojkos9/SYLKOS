from django.db.models.query import QuerySet
from matplotlib.figure import Figure
from rest_framework import generics
from voting.models import Group, Project, Comment, VotingType, Voting, Photo, GroupKey, Vote
from voting.api.permissions import IsAdminOrReadOnly, IsAuthorOrReadOnly, IsGroupAdmin
from voting.api.serializers import CommentSerializer, GroupDetailsSerializer, GroupKeySerializer, GroupSerializer, ProjectSerializer, ProjectSerializer, VotingTypeSerializer, VotingSerializer, PhotoSerializer
from rest_framework import generics, status, viewsets, request
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404, ListCreateAPIView
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.parsers import JSONParser
from voting.api import serializers
from rest_framework.decorators import api_view, permission_classes
from django.db import transaction
import random
from django.http.response import Http404, HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseServerError, HttpResponseForbidden, JsonResponse


class GroupListCreateAPIView(generics.ListCreateAPIView):
    queryset = Group.objects.all().order_by("id")
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GroupDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get_serializer_class(self):
        return GroupDetailsSerializer if self.request.query_params.get('details') == '1' else GroupSerializer


class PhotoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Photo.objects.all().order_by("id")
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PhotoDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all().order_by("id")
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class JoinGroupAPIView(APIView):
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        user = request.user

        group.members.remove(user)
        group.save()

        user.user_groups.remove(group)
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(group, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request: request.Request, pk):
        group = get_object_or_404(Group, pk=pk)
        user = request.user

        try:
            key = request.data["key"]
        except KeyError:
            return HttpResponseForbidden("Key not supplied")

        stored_key: GroupKey = GroupKey.objects.filter(group=group, value=key).first()

        if stored_key:
            stored_key.delete()
        else:
            return HttpResponseForbidden("Invalid key")

        group.members.add(user)
        group.save()

        user.user_groups.add(group)
        user.save()

        serializer_context = {"request": request}
        serializer = self.serializer_class(group, context=serializer_context)

        return Response(serializer.data, status=status.HTTP_200_OK)

KEY_CHARSET = "0123456789"
KEY_LEN = 8
@api_view(["GET"])
@permission_classes([IsGroupAdmin])
def group_gen_keys(request: request.Request, pk: int):
    LIMIT = 999
    count = request.query_params.get("count") or 1
    count = int(count)
    if count > LIMIT:
        return HttpResponseBadRequest(f"count > {LIMIT}")

    group = get_object_or_404(Group.objects.all(), pk=pk)
    keys = ["".join(random.choices(KEY_CHARSET, k=KEY_LEN)) for _ in range(count)]
    for k in keys:
        GroupKey(group=group, value=k, handed_over=True).save()
    return JsonResponse(keys, safe=False)

class ListGroupKeys(generics.ListAPIView):
    permission_classes=(IsAdminUser,)
    serializer_class=GroupKeySerializer
    def get_queryset(self):
        return GroupKey.objects.filter(group=Group.objects.get(pk=self.kwargs['pk']))

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
    permission_classes = []

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Comment.objects.filter(project=pk).order_by("-created_at")


class CommentRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


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
    permission_classes = [IsAuthenticatedOrReadOnly]

import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from io import BytesIO
from datetime import datetime

import matplotlib
matplotlib.use('Agg')

@api_view(['GET'])
def voting_stats(request, **kwargs):
    voting: Voting = get_object_or_404(Voting, pk=kwargs.get('pk'))
    projects: QuerySet[Project] = Project.objects.filter(voting=voting)
    votes: list[tuple[int, int, datetime]] = Vote.objects.filter(voting=voting) \
        .order_by("date") \
        .values_list("project", "points", "date")

    plot_data = {p.pk: (p.name, [(voting.start_date, 0)]) for p in projects}

    for pid, value, date in votes:
        if not value: continue
        date_points  = plot_data[pid][1]
        last_date, last_value = date_points[-1]
        new_point = (date, last_value + value)

        # Aggregate by day:
        if date.date() == last_date.date():
            date_points.pop()

        date_points.append(new_point)

    fig, ax = plt.subplots()
    max_points = 0
    for name, date_points in plot_data.values():
        dates, points = zip(*date_points)
        print(name, dates, points)
        ax.plot(dates, points, 'o-', label=name)
        max_points = max(points[-1], max_points)

    ax.tick_params('x', rotation=90)
    ax.xaxis.set_major_formatter(DateFormatter('%d/%m'))
    ax.set_yticks(range(0, max_points+1))

    buf: BytesIO = BytesIO()
    fig.legend()
    fig.savefig(buf, format='svg')

    return HttpResponse(buf.getvalue().decode('utf-8'))


class VoteView(ListCreateAPIView):
    parser_classes = [JSONParser]
    permission_classes = [IsAuthenticated]

    def post(self, q: request.Request):
        s = serializers.VoteSerializer(data=q.data, context={"request": q})
        try:
            if s.is_valid(raise_exception=True):
                votes = s.save()
                return HttpResponse(", ".join([str(x) for x in votes]))
            return HttpResponseBadRequest("Invalid request")
        except Exception as e:
            return HttpResponseServerError(e)

class DeleteVoteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        votes = Vote.objects.filter(user=request.user, voting=pk)
        if votes:
            votes.delete()
            return HttpResponse("OK")
        else:
            return HttpResponseNotFound()
