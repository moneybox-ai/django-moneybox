from django.contrib import admin
from wallet.models.currency import Currency, CurrencyRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "code",
        "name",
        "type",
        "created_at",
        "updated_at",
    )
    list_filter = ("type", "created_at", "updated_at")
    search_fields = ("name", "code")
    date_hierarchy = "updated_at"


@admin.register(CurrencyRate)
class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "currency",
        "rate",
        "created_at",
        "updated_at",
    )
    list_filter = ("currency__type", "created_at", "updated_at")
    date_hierarchy = "created_at"
