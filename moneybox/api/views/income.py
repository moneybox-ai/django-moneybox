from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from api.serializers import IncomeCategorySerializer, IncomeSerializer
from wallet.models.income import IncomeCategory, Income


@extend_schema(tags=["Incomes"])
class IncomeCategoryViewSet(ModelViewSet):
    queryset = IncomeCategory.objects.order_by("pk")
    serializer_class = IncomeCategorySerializer


@extend_schema(tags=["Incomes"])
class IncomeViewSet(ModelViewSet):
    queryset = Income.objects.order_by("pk")
    serializer_class = IncomeSerializer
