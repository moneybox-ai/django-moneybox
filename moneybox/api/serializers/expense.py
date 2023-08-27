from rest_framework.serializers import ModelSerializer

from wallet.models.expense import ExpenseCategory, Expense


class ExpenseCategorySerializer(ModelSerializer):
    class Meta:
        model = ExpenseCategory
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> upstream/main


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> upstream/main
