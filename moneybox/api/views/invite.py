import random
from datetime import timedelta

from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.permissions import IsAuthenticated
from api.serializers.invite import InviteSerializer
from wallet.models.group import Group
from wallet.models.invite import Invite


@extend_schema(tags=["Invites"])
class InviteViewSet(ModelViewSet):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer

    @action(detail=False, methods=("POST",), permission_classes=(IsAuthenticated,))
    def invite(self, request):  # TODO scheme for swagger
        """Create invite code."""
        user_token = request.user.token
        group = Group.objects.filter(members__token=user_token).first()
        if group:
            invite_code = random.randint(1000000, 9999999)
            expires_at = timezone.now() + timedelta(days=7)
            Invite.objects.create(invite_code=invite_code, group=group, expires_at=expires_at)
            return Response({"code": invite_code})
        return Response({"detail": "Group not found"})  # TODO unreal case
