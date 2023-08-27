from rest_framework.viewsets import ModelViewSet

from api.serializers import TransferSerializer
from wallet.models.transfer import Transfer


class TransferViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = Transfer.objects.order_by('pk')
=======
    queryset = Transfer.objects.order_by("pk")
>>>>>>> upstream/main
    serializer_class = TransferSerializer
