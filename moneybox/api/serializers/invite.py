from rest_framework.serializers import ModelSerializer

from api.serializers import GroupSerializer
from wallet.models.invite import Invite


class InviteSerializer(ModelSerializer):
    group = GroupSerializer()

    class Meta:
        model = Invite
        fields = "__all__"
