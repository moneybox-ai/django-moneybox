from uuid import uuid4

from rest_framework import serializers

from api.encryption import encrypt_token
from users.models import APIUser
from wallet.models.group import Group
from wallet.models.invite import Invite


class APIUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = APIUser
        fields = "__all__"


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

    def create(self, validated_data):
        invite_code = validated_data.get("invite_code")
        token = str(uuid4())
        token_db = encrypt_token(token.encode())

        # TODO add default incomes, expenses and wallets by user
        if invite_code:
            group_invite = Invite.objects.filter(invite_code=invite_code).first()
            user = APIUser.objects.create(token=token_db)
            group = group_invite.group
            group.members.add(user)
            group_invite.delete()
        else:
            user = APIUser.objects.create(token=token_db)
            group = Group.objects.create()
            group.members.add(user)
        return user
