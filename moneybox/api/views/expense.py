from rest_framework.viewsets import ModelViewSet

from api.serializers import ExpenseCategorySerializer, ExpenseSerializer
from wallet.models.expense import ExpenseCategory, Expense


class ExpenseCategoryViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = ExpenseCategory.objects.order_by('pk')
=======
    queryset = ExpenseCategory.objects.order_by("pk")
>>>>>>> upstream/main
    serializer_class = ExpenseCategorySerializer


class ExpenseViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = Expense.objects.order_by('pk')
=======
    queryset = Expense.objects.order_by("pk")
>>>>>>> upstream/main
    serializer_class = ExpenseSerializer
