from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import GroupSerializer
from users.models import APIUser
from wallet.models.group import Group


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.order_by("pk")
    serializer_class = GroupSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        user_token = request.user.token
        user = APIUser.objects.get(token=user_token)
        group = Group.objects.create(name=name)
        group.members.add(user)
        serializer = self.serializer_class(group)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
