import pytest
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APIRequestFactory

from core.defs.datetime import convert_date_for_json
from users.models import APIUser
from wallet.models.currency import Currency
from wallet.models.expense import Expense, ExpenseCategory
from wallet.models.group import Group
from wallet.models.income import Income, IncomeCategory
from wallet.models.wallet import Wallet
from api.serializers.report import ReportSerializer
from api.views.report import ReportViewSet

User = get_user_model()


@pytest.fixture
def api_rf():
    return APIRequestFactory()


@pytest.fixture
def user():
    return APIUser.objects.create(token="8db757d5-c7d9-44dc-a7a7-f9cf8e7920dd")


@pytest.fixture
def group(user):
    group = Group.objects.create(name="Test Group")
    group.members.set([user.id])
    return group


@pytest.fixture
def currency():
    return Currency.objects.create(code="RUB", name="Рубль")


@pytest.fixture
def wallet(user, group, currency):
    return Wallet.objects.create(name="Test Wallet", balance=50, created_by=user, group=group, currency=currency)


@pytest.fixture
def income_category(user, group):
    return IncomeCategory.objects.create(name="Test Income Category", group=group, created_by=user)


@pytest.fixture
def expense_category(user, group):
    return ExpenseCategory.objects.create(name="Test Expense Category", group=group, created_by=user)


@pytest.fixture
def income(user, income_category, group, wallet):
    income = Income.objects.create(
        amount=100, category=income_category, created_by=user, group=group, wallet=wallet, comment="Зарплата"
    )
    income.save()
    return income


@pytest.fixture
def expense(user, expense_category, group, wallet):
    expense = Expense.objects.create(
        amount=50, category=expense_category, created_by=user, group=group, wallet=wallet, comment="Такси"
    )
    expense.save()
    return expense


@pytest.mark.django_db
def test_list(api_rf, user):
    request = api_rf.get("/reports/")
    request.user = user

    # Добавляем пользовательский токен в запрос
    token = user.auth_token
    request.META["HTTP_AUTHORIZATION"] = f"Token {token.key}"

    # Получаем ожидаемые значения
    start_date = timezone.now().date()
    end_date = timezone.now().date()
    total_incomes_per, total_incomes = ReportViewSet.get_total_incomes(user, start_date, end_date)
    total_expenses_per, total_expenses = ReportViewSet.get_total_expenses(user, start_date, end_date)
    income_expense_ratio = ReportViewSet.get_income_expense_ratio(total_incomes_per, total_expenses_per)
    category_incomes = ReportViewSet.get_category_incomes(user, start_date, end_date)
    category_expenses = ReportViewSet.get_category_expenses(user, start_date, end_date)

    actual_data = {
        "balance": total_incomes - total_expenses,
        "total_incomes": total_incomes_per,
        "total_expenses": total_expenses_per,
        "income_expense_ratio": income_expense_ratio,
        "category_incomes": category_incomes,
        "category_expenses": category_expenses,
    }

    expected_data = {
        "balance": Decimal("50"),
        "total_incomes": Decimal("100"),
        "total_expenses": Decimal("50"),
        "income_expense_ratio": Decimal("2"),
        "category_incomes": [
            {
                "category__name": "Test Income Category",
                "total_expenses": Decimal("100"),
                "created_at": convert_date_for_json(timezone.now()),
            }
        ],
        "category_expenses": [
            {
                "category__name": "Test Expense Category",
                "total_expenses": Decimal("50"),
                "created_at": convert_date_for_json(timezone.now()),
            }
        ],
    }

    response = ReportViewSet.as_view({"get": "list"})(request)

    assert response.status_code == 200

    assert ReportSerializer(actual_data).data == ReportSerializer(expected_data).data
