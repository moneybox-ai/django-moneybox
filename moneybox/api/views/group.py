from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.serializers import GroupSerializer
from users.models import APIUser
from wallet.models.group import Group


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.order_by("pk")
    serializer_class = GroupSerializer