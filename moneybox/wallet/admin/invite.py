from django.contrib import admin

from wallet.models.invite import Invite


@admin.register(Invite)
class InviteAdmin(admin.ModelAdmin):
    list_display = ("id", "invite_code", "group", "created_at", "updated_at")
    list_filter = ("created_at", "updated_at")
    search_fields = ("name", "group")
    date_hierarchy = "created_at"
