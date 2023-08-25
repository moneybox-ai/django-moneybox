from rest_framework.viewsets import ModelViewSet

from api.serializers import GroupSerializer
from wallet.models.group_models import Group


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.order_by('pk')
    serializer_class = GroupSerializer
