from rest_framework.viewsets import ModelViewSet

from api.serializers import CustomUserSerializer
from users.models import CustomUser


class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.order_by("pk")
    serializer_class = CustomUserSerializer
