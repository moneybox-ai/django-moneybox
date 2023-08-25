from rest_framework.serializers import ModelSerializer

from wallet.models.transfer_models import Transfer


class TransferSerializer(ModelSerializer):
    class Meta:
        model = Transfer
        fields = '__all__'
