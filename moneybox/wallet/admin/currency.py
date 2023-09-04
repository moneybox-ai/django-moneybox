from django.contrib import admin
from wallet.models.currency import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "nominal",
        "name",
        "value",
        "created_at",
        "updated_at"
    )

    list_filter = (
        "code",
        "name",
        "created_at",
        "updated_at",
        "id"
    )
    search_fields = (
        "code",
        "name"
    )
    date_hierarchy = "created_at"


class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "source_currency",
        "target_currency",
        "rate",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "source_currency",
        "target_currency",
        "id",
        "rate",
    )
    date_hierarchy = "created_at"
