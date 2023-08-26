from rest_framework.viewsets import ModelViewSet

from api.serializers import ProfileSerializer
from users.models import Profile


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.order_by('pk')
    serializer_class = ProfileSerializer
