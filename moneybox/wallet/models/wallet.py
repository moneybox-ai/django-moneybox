from django.db import models

from wallet.models.group import Group
from wallet.models.mixins import TimestampMixin, SafeDeletionMixin, SafeDeletionManager
from users.models import APIUser


class Wallet(TimestampMixin, SafeDeletionMixin):
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="Name of the wallet",
        db_index=True,
    )
    balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Balance",
        help_text="Current balance of the wallet",
    )
    created_by = models.ForeignKey(
        APIUser,
        on_delete=models.CASCADE,
        verbose_name="Created by",
        help_text="Owner of the wallet",
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Group",
        help_text="Group that the wallet belongs to",
        db_index=True,
    )
    currency = models.ForeignKey(
        "Currency",
        on_delete=models.CASCADE,
        verbose_name="Currency",
        help_text="Currency of the wallet",
        db_index=True,
    )
    objects = SafeDeletionManager()

    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"
