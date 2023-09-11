from typing import Any
from uuid import uuid4

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from moneybox.settings import F
from wallet.models.timestamp import TimestampMixin


class APIUser(TimestampMixin):
    token = models.TextField(primary_key=True)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class CustomUserManager(UserManager):
    def create_superuser(self, username: str, password: str | None, new_api_user=None, **extra_fields: Any) -> Any:
        if new_api_user is None:
            token_new = str(uuid4())
            token_encrypted = F.encrypt(token_new.encode()).decode()
            new_api_user = APIUser.objects.create(token=token_encrypted)

        user = self.create_user(
            username=username, password=password, api_user=new_api_user, is_staff=True, is_superuser=True
        )
        user.save(using=self._db)
        return user


class User(AbstractUser):
    api_user = models.OneToOneField(APIUser, on_delete=models.CASCADE, related_name="user_for_admin_site")

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "администратор"
        verbose_name_plural = "администраторы"

    objects = CustomUserManager()
