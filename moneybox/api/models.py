from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
        help_text="Date and time of creation",
        db_index=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at",
        help_text="Date and time of last update",
        db_index=True,
    )

    class Meta:
        abstract = True
        verbose_name = "Timestamp Mixin"
        verbose_name_plural = "Timestamp Mixins"


class Profile(TimestampMixin):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="User associated with the profile",
        db_index=True,
    )
    first_name = models.CharField(
        max_length=255, verbose_name="First name", help_text="First name of the user"
    )
    last_name = models.CharField(
        max_length=255, verbose_name="Last name", help_text="Last name of the user"
    )
    email = models.EmailField(verbose_name="Email", help_text="Email of the user")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class Group(TimestampMixin):
    name = models.CharField(
        max_length=255,
        verbose_name="Group name",
        help_text="Name of the group",
        db_index=True,
    )
    members = models.ManyToManyField(
        Profile,
        related_name="groups",
        verbose_name="Group members",
        help_text="Members of the group",
        db_index=True,
    )

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"


class Wallet(TimestampMixin):
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
        Profile,
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="Owner of the wallet",
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Group",
        help_text="Group that the wallet belongs to",
        db_index=True,
    )

    class Meta:
        verbose_name = "Wallet"
        verbose_name_plural = "Wallets"


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


class ExpenseCategory(TimestampMixin):
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
        Profile,
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="The user who created this expense category",
    )

    class Meta:
        verbose_name = "Expense Category"
        verbose_name_plural = "Expense Categories"


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


class Expense(TimestampMixin):
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Amount of expense"
    )
    category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.CASCADE,
        verbose_name="Expense category",
        db_index=True,
    )
    comment = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Comment on expense"
    )
    created_by = models.ForeignKey(
        Profile, on_delete=models.CASCADE, verbose_name="User who made the expense"
    )
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

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"


class Transfer(TimestampMixin):
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
        Profile,
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="The user who made the transfer.",
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        verbose_name="Group",
        help_text="The group to which the transfer belongs.",
        db_index=True,
    )

    class Meta:
        verbose_name = "Transfer"
        verbose_name_plural = "Transfers"


class Currency(TimestampMixin):
    code = models.CharField(
        max_length=3,
        unique=True,
        verbose_name="Currency Code",
        help_text='The unique code for this currency, e.g. "USD" for US dollars',
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Currency Name",
        help_text='The name of the currency, e.g. "US Dollar"',
    )

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"


class CurrencyRate(TimestampMixin):
    source_currency = models.ForeignKey(
        Currency,
        related_name="source_currency",
        on_delete=models.CASCADE,
        verbose_name="Source Currency",
        help_text="The currency from which the exchange rate is being calculated.",
    )
    target_currency = models.ForeignKey(
        Currency,
        related_name="target_currency",
        on_delete=models.CASCADE,
        verbose_name="Target Currency",
        help_text="The currency to which the exchange rate is being calculated.",
    )
    rate = models.DecimalField(
        max_digits=10,
        decimal_places=4,
        verbose_name="Exchange Rate",
        help_text="The rate at which the source currency can be exchanged for the target currency.",
    )

    class Meta:
        verbose_name = "Currency rate"
        verbose_name_plural = "Currency rates"
