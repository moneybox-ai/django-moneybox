from rest_framework.viewsets import ModelViewSet

from api.serializers import ProfileSerializer
from users.models import Profile


class ProfileViewSet(ModelViewSet):
<<<<<<< HEAD
    queryset = Profile.objects.order_by('pk')
=======
    queryset = Profile.objects.order_by("pk")
>>>>>>> upstream/main
    serializer_class = ProfileSerializer
