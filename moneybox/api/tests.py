from decimal import Decimal

import pytest
from django.contrib.auth import get_user_model
from django.utils import timezone
from rest_framework.test import APIRequestFactory

from api.serializers.report import ReportSerializer
from api.views.report import ReportViewSet
from core.datetime import convert_date_for_json
from users.models import Profile
from wallet.models.currency import Currency
from wallet.models.expense import Expense, ExpenseCategory
from wallet.models.group import Group
from wallet.models.income import Income, IncomeCategory
from wallet.models.wallet import Wallet

User = get_user_model()


@pytest.fixture
def api_rf():
    return APIRequestFactory()


@pytest.fixture
def user():
    return User.objects.create(username='testuser')


@pytest.fixture
def profile(user):
    return Profile.objects.create(user=user,
                                  first_name='test_first_name',
                                  last_name='test_last_name',
                                  email='testemail@mail.ru')


@pytest.fixture
def group(user):
    group = Group.objects.create(name='Test Group')
    group.members.set([user.id])
    return group


@pytest.fixture
def currency():
    return Currency.objects.create(
        code='RUB',
        name='Рубль'
    )


@pytest.fixture
def wallet(profile, group, currency):
    return Wallet.objects.create(
        name='Test Wallet',
        balance=50,
        created_by=profile,
        group=group,
        currency=currency
    )


@pytest.fixture
def income_category(profile, group):
    return IncomeCategory.objects.create(
        name='Test Income Category',
        group=group,
        created_by=profile
    )


@pytest.fixture
def expense_category(profile, group):
    return ExpenseCategory.objects.create(
        name='Test Expense Category',
        group=group,
        created_by=profile
    )


@pytest.fixture
def income(profile, income_category, group, wallet):
    income = Income.objects.create(
        amount=100,
        category=income_category,
        created_by=profile,
        group=group,
        wallet=wallet,
        comment='Зарплата'
    )
    print('Доход:', income.amount)
    print('Группы:', income.group.id)
    income.save()
    return income


@pytest.fixture
def expense(profile, expense_category, group, wallet):
    expense = Expense.objects.create(
        amount=50,
        category=expense_category,
        created_by=profile,
        group=group,
        wallet=wallet,
        comment='Такси'
    )
    print('Расход:', expense.amount)
    print('Группы:', expense.group.id)
    expense.save()
    return expense


@pytest.mark.django_db
def test_list(api_rf, user, profile, income, expense, group):
    request = api_rf.get('/reports/')
    request.user = user

    # Добавляем пользовательский токен в запрос
    token = user.auth_token
    request.META['HTTP_AUTHORIZATION'] = f'Token {token.key}'

    # Получаем ожидаемые значения
    start_date = timezone.now().date()
    end_date = timezone.now().date()
    total_incomes_per, total_incomes = ReportViewSet.get_total_incomes(profile,
                                                                       start_date,
                                                                       end_date)
    total_expenses_per, total_expenses = ReportViewSet.get_total_expenses(
        profile, start_date, end_date)
    income_expense_ratio = ReportViewSet.get_income_expense_ratio(
        total_incomes_per, total_expenses_per)
    category_incomes = ReportViewSet.get_category_incomes(profile, start_date,
                                                          end_date)
    category_expenses = ReportViewSet.get_category_expenses(profile,
                                                            start_date,
                                                            end_date)

    actual_data = {
        "balance": total_incomes - total_expenses,
        "total_incomes": total_incomes_per,
        "total_expenses": total_expenses_per,
        "income_expense_ratio": income_expense_ratio,
        "category_incomes": category_incomes,
        "category_expenses": category_expenses,
    }

    expected_data = {
        'balance': Decimal('50'),
        'total_incomes': Decimal('100'),
        'total_expenses': Decimal('50'),
        'income_expense_ratio': Decimal('2'),
        'category_incomes': [{'category__name': 'Test Income Category',
                              'total_expenses': Decimal('100'),
                              'created_at': convert_date_for_json(
                                  timezone.now())}],
        'category_expenses': [{'category__name': 'Test Expense Category',
                               'total_expenses': Decimal('50'),
                               'created_at': convert_date_for_json(
                                   timezone.now())}]
    }

    # Call the list method to get the response
    response = ReportViewSet.as_view({'get': 'list'})(request)

    # Assert that the response has a status code of 200
    assert response.status_code == 200

    # Прогоняем данные через ReportSerializer
    # actual_data = ReportSerializer(actual_data).data
    # actual_data.is_valid()

    # Сравниваем сериализованные данные с ожидаемыми данными
    print(ReportSerializer(actual_data).data)
    print(expected_data)
    assert ReportSerializer(actual_data).data == ReportSerializer(expected_data).data

    # # Assert that the serializer class used is ReportSerializer
    # assert response.data['report_data'] == ReportSerializer(expected_data).data
