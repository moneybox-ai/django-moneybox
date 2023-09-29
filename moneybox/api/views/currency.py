from api.permissions import IsAdminOrReadOnly
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from api.serializers import CurrencySerializer, CurrencyRateSerializer
from wallet.models.currency import Currency, CurrencyRate
from rest_framework import filters
from rest_framework.decorators import action
from django.http import HttpResponse
from datetime import datetime
from core.defs.datetime import RATE_DATE_FORMAT


@extend_schema(tags=["Currency"])
class CurrencyViewSet(ModelViewSet):
    """List of currencies or add new currency"""

    queryset = Currency.objects.order_by("pk")
    serializer_class = CurrencySerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = (
        "code",
        "name",
    )
    permission_classes = (IsAdminOrReadOnly,)


@extend_schema(tags=["Currency"])
class CurrencyRateViewSet(ModelViewSet):
    queryset = CurrencyRate.objects.order_by("pk")
    serializer_class = CurrencyRateSerializer

    @action(
        detail=False,
        methods=["GET"],
    )
    def get_rate(self, request):
        currency_from = request.query_params.get("currency_from")
        currency_to = request.query_params.get("currency_to")
        date = request.query_params.get("date")
        date = datetime.strptime(date, RATE_DATE_FORMAT).date()
        rate = CurrencyRate.get_exchange_rate(currency_from, currency_to, date)
        return HttpResponse(rate)
