from django.db import models


class TimestampMixin(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at",
        help_text="Date and time of creation",
        db_index=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at",
        help_text="Date and time of last update",
        db_index=True,
    )

    class Meta:
        abstract = True
        verbose_name = "Timestamp Mixin"
        verbose_name_plural = "Timestamp Mixins"
