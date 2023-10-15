from rest_framework import serializers

from users.models import APIUser
from wallet.models.invite import Invite


class APIUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIUser
        fields = ("token",)


class SignupSerializer(serializers.Serializer):
    """Create token and add user to the group."""

    invite_code = serializers.IntegerField(required=False)

    def validate(self, data):
        invite_code = data.get("invite_code")
        if not invite_code:
            return data
        group_invite = Invite.objects.filter(invite_code=invite_code).first()
        if not group_invite or group_invite.is_expired:
            raise serializers.ValidationError("Invalid invite code")
        return data
