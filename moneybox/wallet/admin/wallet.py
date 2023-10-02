from django.contrib import admin

from wallet.models.wallet import Wallet


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "balance",
        "group",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"
