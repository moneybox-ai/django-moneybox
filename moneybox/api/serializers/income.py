from rest_framework.serializers import ModelSerializer

from wallet.models.income import IncomeCategory, Income


class IncomeCategorySerializer(ModelSerializer):
    class Meta:
        model = IncomeCategory
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> upstream/main


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
<<<<<<< HEAD
        fields = '__all__'
=======
        fields = "__all__"
>>>>>>> upstream/main
