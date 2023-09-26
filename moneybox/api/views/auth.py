from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api.serializers.user import SignupSerializer
from users.models import APIUser


@api_view(("POST",))
@permission_classes((AllowAny,))
def signup(request):  # TODO There is a error like unable to guess serializer, fix it
    serializer = SignupSerializer(data=request.data)

    if serializer.is_valid():
        user = serializer.save()
        return Response({"token": user.token}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(("POST",))
@permission_classes((AllowAny,))
def signin(request):  # TODO There is a error like unable to guess serializer, fix it
    token_to_compare = request.data["token"]
    if APIUser.objects.filter(token=token_to_compare).exists():
        return Response(status=status.HTTP_200_OK)
    return Response({"error": "no such token exists"}, status.HTTP_401_UNAUTHORIZED)


@api_view(("GET",))
def get_token(request):  # TODO There is a error like unable to guess serializer, fix it
    auth_header = request.headers["Authorization"]
    token = auth_header.split(" ")[1]
    return Response({"token": token}, status.HTTP_200_OK)
