from rest_framework.serializers import ModelSerializer

from wallet.models import IncomeCategory, Income


class IncomeCategorySerializer(ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = '__all__'


class IncomeSerializer(ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'
