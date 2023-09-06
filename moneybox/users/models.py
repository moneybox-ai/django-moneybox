import os
from uuid import uuid4

from cryptography.fernet import Fernet
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from wallet.models.timestamp import TimestampMixin

KEY = os.getenv("FERNET_KEY")
f = Fernet(KEY.encode())


class APIUser(TimestampMixin):
    token = models.TextField(primary_key=True)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class CustomUserManager(UserManager):
    def create_superuser(self, username: str, password: str | None):
        uuid_str = str(uuid4())
        uuid_bytes = uuid_str.encode()
        token_bytes = f.encrypt(uuid_bytes)
        token_str = token_bytes.decode()
        new_api_user = APIUser.objects.create(token=token_str)

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
