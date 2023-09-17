from django.contrib import admin

from wallet.models.wallet import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "name",
        "balance",
        "created_by",
        "group",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "created_by",
        "group",
        "id",
        "name",
        "balance",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"
