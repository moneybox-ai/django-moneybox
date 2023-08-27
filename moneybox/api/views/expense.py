from rest_framework.viewsets import ModelViewSet

from api.serializers import ExpenseCategorySerializer, ExpenseSerializer
from wallet.models.expense import ExpenseCategory, Expense


class ExpenseCategoryViewSet(ModelViewSet):
    queryset = ExpenseCategory.objects.order_by("pk")
    serializer_class = ExpenseCategorySerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.order_by("pk")
    serializer_class = ExpenseSerializer
