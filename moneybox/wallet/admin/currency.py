from django.contrib import admin


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at", "code", "name", "cbr_code", "value")
    list_filter = ("created_at", "updated_at", "id", "code", "name", "cbr_code", "value")
    search_fields = ("name",)
    date_hierarchy = "created_at"


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
