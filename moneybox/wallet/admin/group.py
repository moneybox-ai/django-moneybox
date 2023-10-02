from django.contrib import admin

from wallet.models.group import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    raw_id_fields = ("members",)
    date_hierarchy = "created_at"
