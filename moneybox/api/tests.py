import pytest
from decimal import Decimal

from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APIRequestFactory

from api.serializers.report import ReportSerializer
from api.views.auth import decrypt_ciphertext, encrypt_token
from api.views.report import ReportViewSet
from core.defs.datetime import convert_date_to_datetime_format
from users.models import APIUser
from wallet.models.currency import Currency
from wallet.models.expense import Expense, ExpenseCategory
from wallet.models.group import Group
from wallet.models.income import Income, IncomeCategory
from wallet.models.wallet import Wallet

User = get_user_model()


class TestReport:
    token = "8db757d5-c7d9-44dc-a7a7-f9cf8e7920dd"

    @pytest.fixture
    def api_rf(self):
        return APIRequestFactory()

    @pytest.fixture
    def user(self):
        return APIUser.objects.create(token=encrypt_token(self.token.encode()))

    @pytest.fixture
    def group(self, user):
        group = Group.objects.create()
        group.members.add(user)
        return group

    @pytest.fixture
    def currency(self):
        return Currency.objects.create()

    @pytest.fixture
    def wallet(self, user, group, currency):
        return Wallet.objects.create(name="Test Wallet", balance=50, created_by=user, group=group, currency=currency)

    @pytest.fixture
    def income_category(self, user, group):
        return IncomeCategory.objects.create(name="Test Income Category", group=group, created_by=user)

    @pytest.fixture
    def expense_category(self, user, group):
        return ExpenseCategory.objects.create(name="Test Expense Category", group=group, created_by=user)

    @pytest.fixture
    def income(self, user, income_category, group, wallet):
        income = Income.objects.create(
            amount=100, category=income_category, created_by=user, group=group, wallet=wallet, comment="Зарплата"
        )
        income.save()
        return income

    @pytest.fixture
    def expense(self, user, expense_category, group, wallet):
        expense = Expense.objects.create(
            amount=50, category=expense_category, created_by=user, group=group, wallet=wallet, comment="Такси"
        )
        expense.save()
        return expense

    @pytest.mark.django_db
    def test_list(self, api_rf, user, group):
        request = api_rf.get("/reports/")
        request.user = user

        request.META["HTTP_AUTHORIZATION"] = f"Token {decrypt_ciphertext(user.token)}"

        start_date = timezone.now().date()
        end_date = timezone.now().date()
        total_incomes_per, total_incomes = ReportViewSet.get_total_incomes(group, start_date, end_date)
        total_expenses_per, total_expenses = ReportViewSet.get_total_expenses(group, start_date, end_date)
        income_expense_ratio = ReportViewSet.get_income_expense_ratio(total_incomes_per, total_expenses_per)
        category_incomes = ReportViewSet.get_category_incomes(user.pk, start_date, end_date)
        category_expenses = ReportViewSet.get_category_expenses(user.pk, start_date, end_date)

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
                    "created_at": convert_date_to_datetime_format(timezone.now()),
                }
            ],
            "category_expenses": [
                {
                    "category__name": "Test Expense Category",
                    "total_expenses": Decimal("50"),
                    "created_at": convert_date_to_datetime_format(timezone.now()),
                }
            ],
        }

        response = ReportViewSet.as_view({"get": "list"})(request)

        assert response.status_code == 200

        assert ReportSerializer(actual_data).data == ReportSerializer(expected_data).data


class TestEncryption:
    token = "8db757d5-c7d9-44dc-a7a7-f9cf8e7920dd"
    token_encrypted_pt_1 = (
        b"\x01x}@\xcc\x83\xccr\x1da\xafA\x04\xa0\xa6\xbc\xc4,\xc5\xc0\x9d\x1b#1\xec\xcdz\x9b\x9b\x96"
    )
    token_encrypted_pt_2 = b"1\x88\xf4\x8d\xb6bv\xb0e\x9f|KU\xb77\xecK\xd3\x06M\xee=\x96\xc8\x1b\xc3u"
    token_encrypted = token_encrypted_pt_1 + token_encrypted_pt_2

    def test_encrypt_token(self):
        assert encrypt_token(self.token.encode()) == self.token_encrypted

    def test_decrypt_ciphertext(self):
        assert decrypt_ciphertext(self.token_encrypted) == self.token
