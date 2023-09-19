import sys

from typing import Any
from uuid import uuid4

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from wallet.models.timestamp import TimestampMixin


class APIUser(TimestampMixin):
    token = models.TextField(primary_key=True)
    invite_code = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name = "API User"
        verbose_name_plural = "API Users"

    def __str__(self):
        return self.token


class CustomUserManager(UserManager):
    # TODO check and fix signature of parent method
    def create_superuser(self, username: str, password: str | None, **extra_fields: Any) -> "User":
        token_new = str(uuid4())
        new_api_user = APIUser.objects.create(token=token_new)

        user = self.create_user(
            username=username, password=password, api_user=new_api_user, is_staff=True, is_superuser=True
        )
        user.save(using=self._db)
        token = user.api_user.token
        sys.stdout.write(f"API user token: {token}\n")
        return user


class User(AbstractUser):
    api_user = models.OneToOneField(APIUser, on_delete=models.CASCADE, related_name="admin_user")

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Administrator"
        verbose_name_plural = "Administrators"

    objects = CustomUserManager()
