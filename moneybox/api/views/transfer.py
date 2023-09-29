from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from api.serializers import TransferSerializer
from wallet.models.transfer import Transfer


@extend_schema(tags=["Transfers"])
class TransferViewSet(ModelViewSet):
    queryset = Transfer.objects.order_by("pk")
    serializer_class = TransferSerializer
