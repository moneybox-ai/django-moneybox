from rest_framework.viewsets import ModelViewSet

from api.serializers import TransferSerializer
from wallet.models import Transfer


class TransferViewSet(ModelViewSet):
    queryset = Transfer.objects.order_by('pk')
    serializer_class = TransferSerializer
