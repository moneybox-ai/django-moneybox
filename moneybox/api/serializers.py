from rest_framework.serializers import ModelSerializer
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


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class GroupSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class WalletSerializer(ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"


class IncomeCategorySerializer(ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = "__all__"


class ExpenseCategorySerializer(ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = "__all__"


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = "__all__"


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"


class TransferSerializer(ModelSerializer):
    class Meta:
        model = Transfer
        fields = "__all__"


class CurrencySerializer(ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class CurrencyRateSerializer(ModelSerializer):
    class Meta:
        model = CurrencyRate
        fields = "__all__"
