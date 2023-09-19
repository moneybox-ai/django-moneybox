from uuid import uuid4

from rest_framework import serializers

from users.models import APIUser
from wallet.models.invite import Invite


class APIUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIUser
        fields = "__all__"


class SignupSerializer(serializers.Serializer):
    """Create token and add user to the group."""
    invite_code = serializers.IntegerField(required=False)

    def create(self, validated_data):
        invite_code = validated_data.get("invite_code")

        if invite_code:
            token = str(uuid4())
            user = APIUser.objects.create(token=token)
            group_invite = Invite.objects.filter(invite_code=invite_code).first()
            group = group_invite.group
            group.members.add(user)
            return user
        raise serializers.ValidationError("Invite code is required.")
