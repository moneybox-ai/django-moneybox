from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.encryption import decrypt_ciphertext, encrypt_token
from api.serializers import APIUserSerializer, SignupSerializer
from moneybox.settings import AUTH_HEADER
from users.models import APIUser


@extend_schema(request=SignupSerializer, responses=APIUserSerializer, tags=["Auth"])
@api_view(("POST",))
@permission_classes((AllowAny,))
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        token_for_user = decrypt_ciphertext(user.token)
        return Response({"token": token_for_user}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=APIUserSerializer, responses=None, tags=["Auth"])
@api_view(("POST",))
@permission_classes((AllowAny,))
def signin(request):
    token_passed = request.data["token"]
    token_db = encrypt_token(token_passed.encode())
    if not APIUser.objects.filter(token=token_db).exists():
        return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)
    return Response(status=status.HTTP_200_OK)


@extend_schema(request=None, responses=APIUserSerializer, tags=["Auth"])
@api_view(("GET",))
def get_token(request):
    auth_header = request.headers[AUTH_HEADER]
    token_header = auth_header.split(" ")[1]
    token_db = encrypt_token(token_header.encode())
    if not APIUser.objects.filter(token=token_db).exists():
        return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)
    return Response({"token": token_header}, status.HTTP_200_OK)
