from django.contrib import admin


class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at", "name")
    list_filter = ("created_at", "updated_at", "id", "name")
    raw_id_fields = ("members",)
    search_fields = ("name",)
    date_hierarchy = "created_at"
