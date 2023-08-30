from django.db import models

from wallet.models.timestamp import TimestampMixin
from users.models import CustomUser


class Group(TimestampMixin):
    name = models.CharField(
        max_length=255,
        verbose_name="Group name",
        help_text="Name of the group",
        db_index=True,
    )
    members = models.ManyToManyField(
        CustomUser,
        related_name="groups",
        verbose_name="Group members",
        help_text="Members of the group",
        db_index=True,
    )

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
