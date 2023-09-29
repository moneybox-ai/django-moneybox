from django.contrib import admin
from wallet.models.currency import Currency, CurrencyRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "code",
        "name"
        )
    list_filter = (
        "created_at",
        "updated_at",
        "code",
        "name"
        )
    search_fields = ("name", "code")
    date_hierarchy = "updated_at"


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "currency",
        "rate",
    )
    list_filter = (
        "created_at",
        "currency",
        "id",
        "rate",
    )
    date_hierarchy = "created_at"
