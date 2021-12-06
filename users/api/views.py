from django.db.models.query import QuerySet
from voting.models import Group
from django.http.response import HttpResponse
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from django import http
from users.api.serializers import UserDisplaySerializer, CustomUserSerializer
from rest_framework.permissions import IsAdminUser

from django.views.decorators.csrf import csrf_exempt

class CurrentUserAPIView(APIView):

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)


class CreateCustomUserView(CreateAPIView):
    serializer_class = CustomUserSerializer
    parser_classes = [JSONParser]
    permission_classes = []

    @csrf_exempt  # TODO: Delete
    def post(self, q: Request):
        serializer: CustomUserSerializer = self.serializer_class(data=q.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return http.HttpResponse("OK")
            return http.HttpResponseBadRequest()
        except Exception as e:
            return http.HttpResponseBadRequest(e)

from rest_framework.decorators import api_view, parser_classes, permission_classes
from ..models import CustomUser

@api_view(['POST'])
@permission_classes([IsAdminUser])
def user_grant_rights(request: Request, pk):
    if type(request) == dict:
        request = [request]
    user: CustomUser = get_object_or_404(CustomUser, pk=pk)
    grants = [(get_object_or_404(Group, pk=q.get('group')), q.get('admin')) for q in request.data]
    for (group, make_admin) in grants:
        admins = group.admin_users
        if admins.filter(pk=pk).exists():
            if make_admin == False:
                admins.remove(user)
                group.save()
        elif make_admin:
            admins.add(user)
            group.save()

    d = request.data
    return HttpResponse(f"PK: {pk} req:{d} t:{type(d)} u: {user.username}")