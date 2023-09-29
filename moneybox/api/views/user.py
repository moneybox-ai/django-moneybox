from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from api.serializers import APIUserSerializer
from users.models import APIUser


@extend_schema(tags=["Users"])
class APIUserViewSet(ModelViewSet):
    queryset = APIUser.objects.order_by("pk")
    serializer_class = APIUserSerializer
