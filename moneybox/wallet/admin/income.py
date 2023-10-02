from django.contrib import admin

from wallet.models.income import Income, IncomeCategory


@admin.register(IncomeCategory)
class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
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


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "amount",
        "category",
        "comment",
        "created_by",
        "wallet",
        "group",
        "created_at",
        "updated_at",
    )
    list_filter = (
        "created_at",
        "updated_at",
    )
    date_hierarchy = "created_at"
