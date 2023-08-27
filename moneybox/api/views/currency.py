from rest_framework.viewsets import ModelViewSet

from api.serializers import CurrencySerializer, CurrencyRateSerializer
from wallet.models.currency import Currency, CurrencyRate


class CurrencyViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = Currency.objects.order_by('pk')
=======
    queryset = Currency.objects.order_by("pk")
>>>>>>> upstream/main
    serializer_class = CurrencySerializer


class CurrencyRateViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = CurrencyRate.objects.order_by('pk')
=======
    queryset = CurrencyRate.objects.order_by("pk")
>>>>>>> upstream/main
    serializer_class = CurrencyRateSerializer
