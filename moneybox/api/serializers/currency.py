from rest_framework.serializers import ModelSerializer

from wallet.models.currency import Currency, CurrencyRate


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> upstream/main


class CurrencyRateSerializer(ModelSerializer):
    class Meta:
        model = CurrencyRate
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> upstream/main
