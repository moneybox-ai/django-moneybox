from uuid import uuid4

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.models import APIUser


@api_view(("POST",))
def signup(request):
    token = str(uuid4())
    APIUser.objects.create(token=token)
    return Response({"token": token}, status=status.HTTP_201_CREATED)


@api_view(("POST",))
def signin(request):
    token_to_compare = request.data["token"]
    if APIUser.objects.filter(token=token_to_compare).exists():
        return Response(status=status.HTTP_200_OK)
    return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)


@api_view(("GET",))
def get_token(request):
    auth_header = request.headers["Authorization"]
    token = auth_header.split(" ")[1]
    return Response({"token": token}, status.HTTP_200_OK)
