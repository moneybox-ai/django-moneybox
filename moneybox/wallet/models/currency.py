from django.db import models

from wallet.models.mixins import TimestampMixin, SafeDeletionMixin, SafeDeletionManager
from core.defs.exeptions import RateNotExist


class FiatCurrency:
    RUB = "RUB"


class CryptoCurrency:
    BITCOIN = "bitcoin"
    TON = "ton"
    ETHEREUM = "ethereum"
    USDC = "usdc"


class CurrencyType:
    FIAT = "fiat"
    CRYPTO = "crypto"

    CHOICES = [
        (FIAT, FIAT),
        (CRYPTO, CRYPTO),
    ]


class Currency(TimestampMixin, SafeDeletionMixin):
    code = models.CharField(
        max_length=10,
        unique=True,
        verbose_name="Currency Code",
        help_text="The unique code for this currency",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Currency Name",
        help_text="The name of the currency, e.g. US Dollar",
    )
    type = models.CharField(
        max_length=255,
        verbose_name="Currency Type",
        help_text="The type of the currency, e.g. fiat or crypto",
        choices=CurrencyType.CHOICES,
        default=CurrencyType.FIAT,
    )
    objects = SafeDeletionManager()

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"

    def __str__(self):
        return f"{self.code} {self.name}"


class CurrencyRate(TimestampMixin, SafeDeletionMixin):
    currency = models.ForeignKey(
        Currency,
        related_name="rate",
        on_delete=models.CASCADE,
        verbose_name="Currency",
        help_text="Currency",
        null=True,
        blank=True,
    )
    rate = models.DecimalField(
        max_digits=12,
        decimal_places=5,
        verbose_name="Exchange Rate",
        help_text="The rate at which the source currency" "can be exchanged for the target currency.",
    )
    objects = SafeDeletionManager()

    class Meta:
        verbose_name = "Currency rate"
        verbose_name_plural = "Currency rates"
        get_latest_by = ("created_at",)

    def __repr__(self):
        return f"{self.currency} is {self.rate}"

    @classmethod
    def get_exchange_rate(cls, currency_from, currency_to, date):
        first_value = cls.objects.filter(
            currency=currency_from, created_at__day=date.day, created_at__month=date.month, created_at__year=date.year
        ).latest()
        second_value = cls.objects.filter(
            currency=currency_to, created_at__day=date.day, created_at__month=date.month, created_at__year=date.year
        ).latest()
        if first_value and second_value:
            return round((first_value.rate / second_value.rate), 4)
        raise RateNotExist
