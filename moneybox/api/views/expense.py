from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from api.serializers import ExpenseCategorySerializer, ExpenseSerializer
from wallet.models.expense import ExpenseCategory, Expense


@extend_schema(tags=["Expenses"])
class ExpenseCategoryViewSet(ModelViewSet):
    queryset = ExpenseCategory.objects.order_by("pk")
    serializer_class = ExpenseCategorySerializer


@extend_schema(tags=["Expenses"])
class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.order_by("pk")
    serializer_class = ExpenseSerializer
