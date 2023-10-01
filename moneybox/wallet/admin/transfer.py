from django.contrib import admin

from wallet.models.transfer import Transfer


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "from_wallet",
        "to_wallet",
        "amount",
        "comment",
        "group",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    date_hierarchy = "created_at"
