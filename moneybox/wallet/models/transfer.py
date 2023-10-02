from decimal import Decimal

from django.db import models, transaction

from wallet.models.currency import CurrencyRate
from wallet.models.group import Group
from wallet.models.mixins import TimestampMixin, SafeDeletionMixin, SafeDeletionManager
from wallet.models.wallet import Wallet
from users.models import APIUser


class Transfer(TimestampMixin, SafeDeletionMixin):
    from_wallet = models.ForeignKey(
        Wallet,
        related_name="transfers_from",
        on_delete=models.CASCADE,
        verbose_name="From Wallet",
        help_text="The wallet from which the transfer is made.",
        db_index=True,
    )
    to_wallet = models.ForeignKey(
        Wallet,
        related_name="transfers_to",
        on_delete=models.CASCADE,
        verbose_name="To Wallet",
        help_text="The wallet to which the transfer is made.",
        db_index=True,
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Transfer Amount",
        help_text="The amount of money transferred.",
    )
    comment = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Transfer Comment",
        help_text="Additional comment about the transfer (optional).",
    )
    created_by = models.ForeignKey(
        APIUser,
        on_delete=models.CASCADE,
        verbose_name="Created by",
        help_text="The user who made the transfer.",
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Group",
        help_text="The group to which the transfer belongs.",
        db_index=True,
    )
    objects = SafeDeletionManager()

    class Meta:
        verbose_name = "Transfer"
        verbose_name_plural = "Transfers"

    @transaction.atomic
    def save(self, *args, **kwargs):
        # TODO add checking of current and target currencies
        super().save(*args, **kwargs)
        rate_from = CurrencyRate.objects.get(
            source_currency=self.from_wallet.currency,
            target_currency=self.to_wallet.currency,
        )
        amount_converted = Decimal(self.amount) * rate_from.rate
        self.from_wallet.balance -= self.amount
        self.from_wallet.save()
        self.to_wallet.balance += amount_converted
        self.to_wallet.save()
        self.from_wallet.balance -= self.amount
        self.from_wallet.save()
        self.to_wallet.balance += amount_converted
        self.to_wallet.save()
