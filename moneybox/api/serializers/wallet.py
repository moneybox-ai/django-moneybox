from rest_framework.serializers import ModelSerializer

from wallet.models.wallet import Wallet


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> upstream/main
