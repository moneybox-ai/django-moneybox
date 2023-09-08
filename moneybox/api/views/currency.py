from rest_framework.viewsets import ModelViewSet

from api.serializers import CurrencySerializer, CurrencyRateSerializer
from wallet.models.currency import Currency, CurrencyRate
from rest_framework import filters, permissions


class CurrencyViewSet(ModelViewSet):
    """List of currencies or add new currency"""

    queryset = Currency.objects.order_by("pk")
    serializer_class = CurrencySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "code",
        "name",
    )
    # TODO fix it when the user model is donne. Add from api.permissions import IsAdminOrReadOnly
    permission_classes = (permissions.AllowAny,)


class CurrencyRateViewSet(ModelViewSet):
    queryset = CurrencyRate.objects.order_by("pk")
    serializer_class = CurrencyRateSerializer
