from rest_framework.viewsets import ModelViewSet

from api.serializers import WalletSerializer
from wallet.models.wallet import Wallet


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.order_by("pk")
    serializer_class = WalletSerializer
