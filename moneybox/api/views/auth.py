from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CustomUserSerializer
from users.models import CustomUser


@api_view(("POST",))
def signup(request):
    new_user = CustomUser.objects.create()
    user_uuid = new_user.uuid
    return Response({"uuid": user_uuid}, status=status.HTTP_201_CREATED)


@api_view(("POST",))
def signin(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        token = serializer.validated_data['uuid']
        if CustomUser.objects.filter(uuid=token).exists():
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"Authentication failed": "no such uuid exists"},
                            status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
