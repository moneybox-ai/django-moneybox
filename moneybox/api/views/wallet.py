from rest_framework.viewsets import ModelViewSet

from api.serializers import WalletSerializer
from wallet.models.wallet import Wallet


class WalletViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = Wallet.objects.order_by('pk')
=======
    queryset = Wallet.objects.order_by("pk")
>>>>>>> upstream/main
    serializer_class = WalletSerializer
