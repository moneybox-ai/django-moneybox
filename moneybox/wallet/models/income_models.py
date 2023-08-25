from django.db import models, transaction

from users.models import Profile
from wallet.models.group_models import Group
from wallet.models.timestamp_models import TimestampMixin
from wallet.models.wallet_models import Wallet


class IncomeCategory(TimestampMixin):
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="Name of the income category",
        db_index=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Group",
        help_text="Group that the income category belongs to",
        db_index=True,
    )
    created_by = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="income_categories",
        verbose_name="Created by",
        help_text="Profile that created the income category",
    )

    class Meta:
        verbose_name = "Income Category"
        verbose_name_plural = "Income Categories"


class Income(TimestampMixin):
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Income amount"
    )
    category = models.ForeignKey(
        IncomeCategory,
        on_delete=models.CASCADE,
        verbose_name="Income category",
        db_index=True,
    )
    comment = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Comment on income"
    )
    created_by = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="Income creator"
    )
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        verbose_name="Wallet for income",
        db_index=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Group for income",
        db_index=True,
    )

    class Meta:
        verbose_name = "Income"
        verbose_name_plural = "Incomes"

    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.wallet.balance += self.amount
        self.wallet.save()
