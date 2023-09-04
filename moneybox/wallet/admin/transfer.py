from django.contrib import admin

from wallet.models.transfer import Transfer


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "from_wallet",
        "to_wallet",
        "amount",
        "comment",
        "created_by",
        "group",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "from_wallet",
        "to_wallet",
        "created_by",
        "group",
        "id",
        "amount",
        "comment",
    )
    date_hierarchy = "created_at"
