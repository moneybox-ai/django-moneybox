from django.db import models

from wallet.models.timestamp import TimestampMixin
from core.exeptions import RateNotExist


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

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return f"{self.code} {self.name}"


class CurrencyRate(TimestampMixin):
    currency = models.ForeignKey(
        Currency,
        related_name="currency",
        on_delete=models.CASCADE,
        verbose_name="Currency",
        help_text="Currency",
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
        get_latest_by = ["created_at"]

    def __repr__(self):
        return f"{self.currency} is {self.rate}"

    def get_exchange_rate(self, currency1, currency2, date):
        first_value = CurrencyRate.objects.filter(
            currency=currency1, created_at__day=date.day, created_at__month=date.month, created_at__year=date.year
        ).latest()
        second_value = CurrencyRate.objects.filter(
            currency=currency2, created_at__day=date.day, created_at__month=date.month, created_at__year=date.year
        ).latest()
        if first_value and second_value:
            return round((first_value.rate / second_value.rate), 4)
        raise RateNotExist
