from django.contrib.auth.models import AbstractUser
from django.db import models

from wallet.models.mixins import TimestampMixin, SafeDeletionMixin


class APIUser(TimestampMixin, SafeDeletionMixin):
    token = models.BinaryField()

    class Meta:
        verbose_name = "API User"
        verbose_name_plural = "API Users"

    def __str__(self):
        return f"API User with ID {self.pk}"


class User(AbstractUser):
    """
    The administrator model.
    The 'api_user' field is not required for technical reasons: when creating a superuser using
    the 'createsuperuser' command we need to finish creating a superuser first and only then add
    an API user to the superuser.
    """

    api_user = models.OneToOneField(
        APIUser, on_delete=models.CASCADE, related_name="admin_user", blank=True, null=True
    )

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Administrator"
        verbose_name_plural = "Administrators"
