from django.contrib import admin

from wallet.models.group import Group


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at",)
    list_filter = ("created_at", "updated_at", "id",)
    raw_id_fields = ("members",)
    search_fields = ("id",)
    date_hierarchy = "created_at"
