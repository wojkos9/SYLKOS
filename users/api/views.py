from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.request import Request
from django import http
from users.api.serializers import UserDisplaySerializer, CustomUserSerializer

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
