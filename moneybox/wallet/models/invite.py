from django.utils import timezone

from wallet.models.mixins import TimestampMixin, SafeDeletionMixin, SafeDeletionManager

from django.db import models
from wallet.models.group import Group


class Invite(TimestampMixin, SafeDeletionMixin):
    invite_code = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="invites")
    expires_at = models.DateTimeField()
    objects = SafeDeletionManager()

    class Meta:
        constraints = (
            models.UniqueConstraint(
                fields=(
                    "invite_code",
                    "group",
                ),
                name="unique_invite",
            ),
        )
        verbose_name = "Invite"
        verbose_name_plural = "Invites"

    @property
    def is_expired(self):
        return self.expires_at < timezone.now()
