from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import APIUser, User


@admin.register(APIUser)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("token", "created_at", "updated_at")

    list_filter = ("token", "created_at", "updated_at")
    search_fields = ("token",)
    date_hierarchy = "created_at"


@admin.register(User)
class AbstractUserAdmin(UserAdmin):
    list_display = ("username", "api_user", "email", "first_name", "last_name", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email", "api_user")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("username", "password1", "password2", "is_staff", "is_active")}),
    )
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)
