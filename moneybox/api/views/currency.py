from rest_framework.viewsets import ModelViewSet

from api.serializers import CurrencySerializer, CurrencyRateSerializer
from wallet.models.currency import Currency, CurrencyRate
from rest_framework import filters, permissions
from rest_framework.decorators import action
from django.http import HttpResponse
from datetime import datetime
from core.datetime import RATE_DATE_FORMAT


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

    @action(
        detail=False,
        methods=["GET"],
    )
    def get_rate(self, request):
        currency1 = request.query_params.get("currency_from")
        currency2 = request.query_params.get("currency_to")
        date = request.query_params.get("date")
        date = datetime.strptime(date, RATE_DATE_FORMAT).date()
        crate = CurrencyRate()
        rate = crate.get_exchange_rate(currency1, currency2, date)
        return HttpResponse(rate)
