from rest_framework.viewsets import ModelViewSet

from api.serializers import CurrencySerializer, CurrencyRateSerializer
from wallet.models.currency import Currency, CurrencyRate


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.order_by('pk')
    serializer_class = CurrencySerializer


class CurrencyRateViewSet(ModelViewSet):
    queryset = CurrencyRate.objects.order_by('pk')
    serializer_class = CurrencyRateSerializer
