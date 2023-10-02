from django.db import models, transaction

from wallet.models.group import Group
from wallet.models.mixins import TimestampMixin, SafeDeletionMixin, SafeDeletionManager
from wallet.models.wallet import Wallet
from users.models import APIUser


class ExpenseCategory(TimestampMixin, SafeDeletionMixin):
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="The name of the expense category",
        db_index=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Group",
        help_text="The group this expense category belongs to",
        db_index=True,
    )
    created_by = models.ForeignKey(
        APIUser,
        on_delete=models.CASCADE,
        verbose_name="Created by",
        help_text="The user who created this expense category",
    )
    objects = SafeDeletionManager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Expense Category"
        verbose_name_plural = "Expense Categories"


class Expense(TimestampMixin, SafeDeletionMixin):
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount of expense")
    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.CASCADE,
        verbose_name="Expense category",
        db_index=True,
    )
    comment = models.CharField(max_length=255, blank=True, null=True, verbose_name="Comment on expense")
    created_by = models.ForeignKey(APIUser, on_delete=models.CASCADE, verbose_name="User who made the expense")
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        verbose_name="Wallet used for the expense",
        db_index=True,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Group related to the expense",
        db_index=True,
    )
    objects = SafeDeletionManager()

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

    @transaction.atomic
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.wallet.balance -= self.amount
        self.wallet.save()
