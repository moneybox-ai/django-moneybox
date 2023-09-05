from rest_framework.viewsets import ModelViewSet

from api.serializers import APIUserSerializer
from users.models import APIUser


class APIUserViewSet(ModelViewSet):
    queryset = APIUser.objects.order_by("pk")
    serializer_class = APIUserSerializer
