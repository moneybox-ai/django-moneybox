from uuid import uuid4

from django.db import transaction
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.encryption import decrypt_ciphertext, encrypt_token
from api.serializers import APIUserSerializer, SignupSerializer
from api.utils import add_defaults
from moneybox.settings import AUTH_HEADER
from users.models import APIUser
from wallet.models.invite import Invite


@extend_schema(request=SignupSerializer, responses=APIUserSerializer, tags=["Auth"])
@api_view(("POST",))
@permission_classes((AllowAny,))
@transaction.atomic
def signup(request):
    serializer = SignupSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    invite_code = serializer.validated_data.get("invite_code")
    token = str(uuid4())
    token_db = encrypt_token(token.encode())
    user = APIUser.objects.create(token=token_db)
    token_for_user = decrypt_ciphertext(user.token)

    if invite_code:
        group_invite = Invite.objects.filter(invite_code=invite_code).first()
        group = group_invite.group
        group.members.add(user)
        group_invite.delete()
        return Response({"token": token_for_user}, status=status.HTTP_201_CREATED)

    add_defaults(user=user)

    return Response({"token": token_for_user}, status=status.HTTP_201_CREATED)


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
