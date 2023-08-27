from rest_framework.viewsets import ModelViewSet

from api.serializers import GroupSerializer
from wallet.models.group import Group


class GroupViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = Group.objects.order_by('pk')
=======
    queryset = Group.objects.order_by("pk")
>>>>>>> upstream/main
    serializer_class = GroupSerializer
