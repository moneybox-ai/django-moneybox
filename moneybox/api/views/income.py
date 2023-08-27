from rest_framework.viewsets import ModelViewSet

from api.serializers import IncomeCategorySerializer, IncomeSerializer
from wallet.models.income import IncomeCategory, Income


class IncomeCategoryViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = IncomeCategory.objects.order_by('pk')
=======
    queryset = IncomeCategory.objects.order_by("pk")
>>>>>>> upstream/main
    serializer_class = IncomeCategorySerializer


class IncomeViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = Income.objects.order_by('pk')
=======
    queryset = Income.objects.order_by("pk")
>>>>>>> upstream/main
    serializer_class = IncomeSerializer
