import sys

from uuid import uuid4

from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from api.encryption import decrypt_ciphertext, encrypt_token
from wallet.models.mixins import TimestampMixin, SafeDeletionMixin


class APIUser(TimestampMixin, SafeDeletionMixin):
    token = models.BinaryField()

    class Meta:
        verbose_name = "API User"
        verbose_name_plural = "API Users"

    def __str__(self):
        return f"API User with ID {self.pk}"


class CustomUserManager(UserManager):
    def create_superuser(self, username, password=None, **extra_fields):
        from api.utils import add_defaults

        token_new = str(uuid4())
        token_db = encrypt_token(token_new.encode())
        new_api_user = APIUser.objects.create(token=token_db)

        user = self.create_user(
            username=username, password=password, api_user=new_api_user, is_staff=True, is_superuser=True
        )
        user.save(using=self._db)
        token = decrypt_ciphertext(user.api_user.token)
        sys.stdout.write(f"API user token: {token}\n")
        add_defaults(user=new_api_user)
        return user


class User(AbstractUser):
    api_user = models.OneToOneField(APIUser, on_delete=models.CASCADE, related_name="admin_user")

    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Administrator"
        verbose_name_plural = "Administrators"

    objects = CustomUserManager()
