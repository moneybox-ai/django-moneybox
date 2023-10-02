from django.db import models

from wallet.models.mixins import TimestampMixin, SafeDeletionMixin, SafeDeletionManager
from users.models import APIUser


class Group(TimestampMixin, SafeDeletionMixin):
    members = models.ManyToManyField(
        APIUser,
        related_name="groups",
        verbose_name="Group members",
        help_text="Members of the group",
        db_index=True,
    )
    objects = SafeDeletionManager()

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"

    def __str__(self):
        return str(self.pk)
