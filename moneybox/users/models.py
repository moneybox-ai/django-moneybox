import uuid

from django.db import models

from wallet.models.timestamp import TimestampMixin


class CustomUser(TimestampMixin):

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"
