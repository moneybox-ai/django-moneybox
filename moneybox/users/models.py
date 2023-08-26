from django.contrib.auth import get_user_model

from wallet.models.timestamp import TimestampMixin
from django.db import models

User = get_user_model()


class Profile(TimestampMixin):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="User associated with the profile",
        db_index=True,
    )
    first_name = models.CharField(max_length=255, verbose_name="First name", help_text="First name of the user")
    last_name = models.CharField(max_length=255, verbose_name="Last name", help_text="Last name of the user")
    email = models.EmailField(verbose_name="Email", help_text="Email of the user")

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
