from django.db import models

from wallet.models.timestamp import TimestampMixin


class Currency(TimestampMixin):
    code = models.CharField(
        max_length=3,
        unique=True,
        verbose_name="Currency Code",
<<<<<<< HEAD
        help_text="The unique code for this currency,"
                  "e.g. 'USD' for US dollars",
=======
        help_text="The unique code for this currency," "e.g. 'USD' for US dollars",
>>>>>>> upstream/main
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
<<<<<<< HEAD
        help_text="The currency from which"
                  "the exchange rate is being calculated.",
=======
        help_text="The currency from which" "the exchange rate is being calculated.",
>>>>>>> upstream/main
    )
    target_currency = models.ForeignKey(
        Currency,
        related_name="target_currency",
        on_delete=models.CASCADE,
        verbose_name="Target Currency",
<<<<<<< HEAD
        help_text="The currency to which"
                  "the exchange rate is being calculated.",
=======
        help_text="The currency to which" "the exchange rate is being calculated.",
>>>>>>> upstream/main
    )
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name="Exchange Rate",
<<<<<<< HEAD
        help_text="The rate at which the source currency"
                  "can be exchanged for the target currency.",
=======
        help_text="The rate at which the source currency" "can be exchanged for the target currency.",
>>>>>>> upstream/main
    )

    class Meta:
        verbose_name = "Currency rate"
        verbose_name_plural = "Currency rates"
