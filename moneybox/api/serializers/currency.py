from rest_framework.serializers import ModelSerializer

from wallet.models.currency import Currency, CurrencyRate


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class CurrencyRateSerializer(ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = '__all__'
