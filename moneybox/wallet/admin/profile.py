from django.contrib import admin


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "user",
        "first_name",
        "last_name",
        "email",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "user",
        "id",
        "first_name",
        "last_name",
        "email",
    )
    date_hierarchy = "created_at"
