from uuid import uuid4

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from moneybox.settings import F
from users.models import APIUser


@api_view(("POST",))
def signup(request):
    token = str(uuid4())
    token_encrypted = F.encrypt(token.encode()).decode()
    APIUser.objects.create(token=token_encrypted)
    return Response({"token": token}, status=status.HTTP_201_CREATED)


@api_view(("POST",))
def signin(request):
    token_to_compare = request.data["token"]
    api_users = APIUser.objects.all()
    for api_user in api_users:
        token_encrypted = api_user.token
        token_decrypted = F.decrypt(token_encrypted.encode()).decode()
        if token_decrypted == token_to_compare:
            return Response(status=status.HTTP_200_OK)
    return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)


def authenticate(request):
    if request.headers["Authorization"]:
        auth_header = request.headers["Authorization"]
        token_from_header = auth_header.split(" ")[1]
        api_users = APIUser.objects.all()
        for api_user in api_users:
            token_encrypted = api_user.token
            token_decrypted = F.decrypt(token_encrypted.encode()).decode()
            if token_decrypted == token_from_header:
                return Response(status=status.HTTP_200_OK)
        return Response({"error": "authentication failed: token not recognized"}, status.HTTP_403_FORBIDDEN)
    return Response({"error": "authentication failed: no token provided"}, status.HTTP_403_FORBIDDEN)


@api_view(("GET",))
def get_token(request):
    auth_header = request.headers["Authorization"]
    token = auth_header.split(" ")[1]
    return Response({"token": token}, status.HTTP_200_OK)
