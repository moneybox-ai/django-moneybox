from rest_framework.viewsets import ModelViewSet

from api.serializers import IncomeCategorySerializer, IncomeSerializer
from wallet.models.income import IncomeCategory, Income


class IncomeCategoryViewSet(ModelViewSet):
    queryset = IncomeCategory.objects.order_by('pk')
    serializer_class = IncomeCategorySerializer


class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.order_by('pk')
    serializer_class = IncomeSerializer
