from django.db import models

from wallet.models.timestamp import TimestampMixin


class Currency(TimestampMixin):
    code = models.CharField(
        max_length=3,
        unique=True,
        verbose_name="Currency Code",
        help_text="The unique code for this currency",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Currency Name",
        help_text="The name of the currency, e.g. US Dollar",
    )

    nominal = models.CharField(
        max_length=15,
        default='0',
        verbose_name="Currency Nominal for rates",
        help_text="Currency denomination for exchange rate conversion",
    )

    value = models.CharField(
        max_length=15,
        default='0',
        verbose_name="Currency exchange rate",
        help_text='Currency value for exchange rate"',
    )

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return f"{self.code} {self.name}"


class CurrencyRate(TimestampMixin):
    source_currency = models.ForeignKey(
        Currency,
        related_name="source_currency",
        on_delete=models.CASCADE,
        verbose_name="Source Currency",
        help_text="The currency from which" "the exchange rate is being calculated.",
    )
    target_currency = models.ForeignKey(
        Currency,
        related_name="target_currency",
        on_delete=models.CASCADE,
        verbose_name="Target Currency",
        help_text="The currency to which" "the exchange rate is being calculated.",
    )
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name="Exchange Rate",
        help_text="The rate at which the source currency" "can be exchanged for the target currency.",
    )

    class Meta:
        verbose_name = "Currency rate"
        verbose_name_plural = "Currency rates"
