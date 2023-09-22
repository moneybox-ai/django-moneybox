import uuid

from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.crypto_temp import encrypt_token
from api.serializers import APIUserSerializer
from moneybox.settings import AUTH_HEADER
from users.models import APIUser


@extend_schema(request=None, responses=APIUserSerializer)
@api_view(("POST",))
@permission_classes((AllowAny,))
def signup(request):
    token_str = str(uuid.uuid4())
    token_db = encrypt_token(token_str.encode())
    APIUser.objects.create(token=token_db)
    return Response({"token": token_str}, status=status.HTTP_201_CREATED)


@extend_schema(request=APIUserSerializer, responses=None)
@api_view(("POST",))
@permission_classes((AllowAny,))
def signin(request):
    token_passed = request.data["token"]
    token_db = encrypt_token(token_passed.encode())
    if not APIUser.objects.filter(token=token_db).exists():
        return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_200_OK)


@extend_schema(request=None, responses=APIUserSerializer)
@api_view(("GET",))
def get_token(request):
    auth_header = request.headers[AUTH_HEADER]
    token_header = auth_header.split(" ")[1]
    token_db = encrypt_token(token_header.encode())
    if not APIUser.objects.filter(token=token_db).exists():
        return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)
    return Response({"token": token_header}, status.HTTP_200_OK)
