from uuid import uuid4

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers import APIUserSerializer
from users.models import APIUser


@extend_schema(request=None, responses=APIUserSerializer)
@api_view(("POST",))
@permission_classes((AllowAny,))
def signup(request):
    token = str(uuid4())
    APIUser.objects.create(token=token)
    return Response({"token": token}, status=status.HTTP_201_CREATED)


@extend_schema(request=APIUserSerializer, responses=None)
@api_view(("POST",))
@permission_classes((AllowAny,))
def signin(request):
    token_to_compare = request.data["token"]
    if APIUser.objects.filter(token=token_to_compare).exists():
        return Response(status=status.HTTP_200_OK)
    return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)


@extend_schema(request=None, responses=APIUserSerializer)
@api_view(("GET",))
def get_token(request):
    auth_header = request.headers["Authorization"]
    token = auth_header.split(" ")[1]
    return Response({"token": token}, status.HTTP_200_OK)
