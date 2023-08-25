from django.db import models

from wallet.models.timestamp_models import TimestampMixin


class Currency(TimestampMixin):
    code = models.CharField(
        max_length=3,
        unique=True,
        verbose_name="Currency Code",
        help_text="The unique code for this currency,"
                  "e.g. 'USD' for US dollars",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Currency Name",
        help_text='The name of the currency, e.g. "US Dollar"',
    )

    @classmethod
    def get_usd(cls):
        return Currency.objects.get(code="USD")

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class CurrencyRate(TimestampMixin):
    source_currency = models.ForeignKey(
        Currency,
        related_name="source_currency",
        on_delete=models.CASCADE,
        verbose_name="Source Currency",
        help_text="The currency from which"
                  "the exchange rate is being calculated.",
    )
    target_currency = models.ForeignKey(
        Currency,
        related_name="target_currency",
        on_delete=models.CASCADE,
        verbose_name="Target Currency",
        help_text="The currency to which"
                  "the exchange rate is being calculated.",
    )
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name="Exchange Rate",
        help_text="The rate at which the source currency"
                  "can be exchanged for the target currency.",
    )

    class Meta:
        verbose_name = "Currency rate"
        verbose_name_plural = "Currency rates"
