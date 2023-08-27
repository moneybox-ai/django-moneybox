from rest_framework.serializers import ModelSerializer

from wallet.models.expense import ExpenseCategory, Expense


class ExpenseCategorySerializer(ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = "__all__"


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields = "__all__"
