from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CustomUserSerializer
from users.models import CustomUser


@api_view(("POST",))
def signup(request):
    new_user = CustomUser.objects.create()
    return Response({"uuid": new_user.uuid}, status=status.HTTP_201_CREATED)


@api_view(("POST",))
def signin(request):
    serializer = CustomUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    token = serializer.validated_data['uuid']
    if CustomUser.objects.filter(uuid=token).exists():
        return Response(status=status.HTTP_200_OK)
    return Response({"error": "no such uuid exists"},
                    status.HTTP_401_UNAUTHORIZED)
