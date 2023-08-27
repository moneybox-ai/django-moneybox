from rest_framework.serializers import ModelSerializer

from wallet.models.wallet import Wallet


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"
