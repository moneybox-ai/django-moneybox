from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsGroupMember
from api.serializers import TransferSerializer
from wallet.models.transfer import Transfer


@extend_schema(tags=["Transfers"])
class TransferViewSet(ModelViewSet):
    queryset = Transfer.objects.order_by("pk")
    serializer_class = TransferSerializer
    permission_classes = (IsGroupMember,)

    def get_queryset(self):
        return Transfer.objects.filter(group__in=self.request.user.groups.all())
