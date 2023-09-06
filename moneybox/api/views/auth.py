import os
from uuid import uuid4

from cryptography.fernet import Fernet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import APIUser

KEY = os.getenv("FERNET_KEY")
f = Fernet(KEY.encode())


@api_view(("POST",))
def signup(request):
    token = str(uuid4())
    token_encrypted = f.encrypt(token.encode()).decode()
    APIUser.objects.create(token=token_encrypted)
    return Response({"token": token}, status=status.HTTP_201_CREATED)


@api_view(("POST",))
def signin(request):
    token_to_compare = request.data["token"]
    api_users = APIUser.objects.all()
    for api_user in api_users:
        token_encrypted = api_user.token
        token_decrypted = f.decrypt(token_encrypted.encode()).decode()
        if token_decrypted == token_to_compare:
            return Response(status=status.HTTP_200_OK)
    return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)


@api_view(("GET",))
def get_token(request):
    auth_header = request.headers["Authorization"]
    token = auth_header.split(" ")[1]
    return Response({"token": token}, status.HTTP_200_OK)
