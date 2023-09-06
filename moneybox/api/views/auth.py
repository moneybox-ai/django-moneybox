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
    uuid_str = str(uuid4())
    uuid_bytes = uuid_str.encode()
    token_bytes = f.encrypt(uuid_bytes)
    token_str = token_bytes.decode()
    APIUser.objects.create(token=token_str)
    return Response({"token": uuid_str}, status=status.HTTP_201_CREATED)


@api_view(("POST",))
def signin(request):
    uuid_str_to_check = request.data["token"]
    queryset = APIUser.objects.all()
    for obj in queryset:
        token_str = obj.token
        token_bytes = token_str.encode()
        uuid_bytes = f.decrypt(token_bytes)
        uuid_str = uuid_bytes.decode()
        if uuid_str == uuid_str_to_check:
            return Response(status=status.HTTP_200_OK)
    return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)
