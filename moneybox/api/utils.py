from datetime import datetime
from django.utils import timezone

from django.db.models import Sum, Max

from core.defs import constants
from core.defs.datetime import convert_date_to_datetime_format
from wallet.models.currency import Currency, FiatCurrency
from wallet.models.expense import ExpenseCategory
from wallet.models.group import Group
from wallet.models.income import IncomeCategory
from wallet.models.wallet import Wallet


def get_start_end_dates(start_date=None, end_date=None):
    if not start_date or not end_date:
        today = timezone.now().date()
        start_of_day = timezone.make_aware(datetime.combine(today, datetime.min.time()))
        end_of_day = timezone.make_aware(datetime.combine(today, datetime.max.time()))
    else:
        start_of_day = timezone.make_aware(datetime.combine(start_date, datetime.min.time()))
        end_of_day = timezone.make_aware(datetime.combine(end_date, datetime.max.time()))

    return start_of_day, end_of_day


def get_category_data(profile, model, start_date=None, end_date=None):
    category_data = (
        model.objects.filter(created_by=profile, created_at__range=get_start_end_dates(start_date, end_date))
        .values("category__name")
        .annotate(total_expenses=Sum("amount"), created_at=Max("created_at"))
        .values("category__name", "total_expenses", "created_at")
    )

    return [{**x, "created_at": convert_date_to_datetime_format(x["created_at"])} for x in category_data]


def get_total_data(group, model, start_date=None, end_date=None):
    total_data_per = (
        getattr(group, model)
        .filter(created_at__range=get_start_end_dates(start_date, end_date))
        .aggregate(total_data=Sum("amount"))
        .get("total_data")
        or 0
    )

    total_data = getattr(group, model).aggregate(total_data=Sum("amount")).get("total_data") or 0

    return total_data_per, total_data


def add_defaults(user):
    """Add expense/income/wallet categories."""

    group = Group.objects.create()
    group.members.add(user)
    currency, _ = Currency.objects.get_or_create(code=FiatCurrency.RUB, name=constants.RUB_NAME)

    expense_categories = [
        ExpenseCategory(name=expense_category, group=group, created_by=user)
        for expense_category in constants.DEFAULT_EXPENSE_CATEGORY
    ]
    ExpenseCategory.objects.bulk_create(expense_categories)

    income_categories = [
        ExpenseCategory(name=income_category, group=group, created_by=user)
        for income_category in constants.DEFAULT_INCOME_CATEGORY
    ]
    IncomeCategory.objects.bulk_create(income_categories)

    wallets = [
        Wallet(
            name=wallet,
            balance=0,
            group=group,
            created_by=user,
            currency=currency,
        )
        for wallet in constants.WALLET_LIST
    ]
    Wallet.objects.bulk_create(wallets)
