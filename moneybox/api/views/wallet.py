from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from api.serializers import WalletSerializer
from wallet.models.wallet import Wallet


@extend_schema(tags=["Wallets"])
class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.order_by("pk")
    serializer_class = WalletSerializer
