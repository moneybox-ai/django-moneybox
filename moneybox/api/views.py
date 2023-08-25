from rest_framework.viewsets import ModelViewSet
from api.serializers import (
    ProfileSerializer,
    GroupSerializer,
    WalletSerializer,
    IncomeCategorySerializer,
    ExpenseCategorySerializer,
    IncomeSerializer,
    ExpenseSerializer,
    TransferSerializer,
    CurrencySerializer,
    CurrencyRateSerializer,
)
from api.models import (
    Profile,
    Group,
    Wallet,
    IncomeCategory,
    ExpenseCategory,
    Income,
    Expense,
    Transfer,
    Currency,
    CurrencyRate,
)


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.order_by("pk")
    serializer_class = ProfileSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.order_by("pk")
    serializer_class = GroupSerializer


class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.order_by("pk")
    serializer_class = WalletSerializer


class IncomeCategoryViewSet(ModelViewSet):
    queryset = IncomeCategory.objects.order_by("pk")
    serializer_class = IncomeCategorySerializer


class ExpenseCategoryViewSet(ModelViewSet):
    queryset = ExpenseCategory.objects.order_by("pk")
    serializer_class = ExpenseCategorySerializer


class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.order_by("pk")
    serializer_class = IncomeSerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.order_by("pk")
    serializer_class = ExpenseSerializer


class TransferViewSet(ModelViewSet):
    queryset = Transfer.objects.order_by("pk")
    serializer_class = TransferSerializer


class CurrencyViewSet(ModelViewSet):
    queryset = Currency.objects.order_by("pk")
    serializer_class = CurrencySerializer


class CurrencyRateViewSet(ModelViewSet):
    queryset = CurrencyRate.objects.order_by("pk")
    serializer_class = CurrencyRateSerializer
