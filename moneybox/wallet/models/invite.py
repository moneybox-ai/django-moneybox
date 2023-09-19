from django.utils import timezone

from wallet.models.timestamp import TimestampMixin

from django.db import models
from wallet.models.group import Group


class Invite(TimestampMixin):
    invite_code = models.IntegerField(unique=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="invites")
    expires_at = models.DateTimeField()

    def is_expired(self):
        return self.expires_at < timezone.now()
