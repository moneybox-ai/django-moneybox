# vim: set fileencoding=utf-8 :
from django.contrib import admin

import api.models as models


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


class GroupAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at", "name")
    list_filter = ("created_at", "updated_at", "id", "name")
    raw_id_fields = ("members",)
    search_fields = ("name",)
    date_hierarchy = "created_at"


class WalletAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "name",
        "balance",
        "created_by",
        "group",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "created_by",
        "group",
        "id",
        "name",
        "balance",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"


class IncomeCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "name",
        "group",
        "created_by",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "group",
        "created_by",
        "id",
        "name",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"


class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "name",
        "group",
        "created_by",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "group",
        "created_by",
        "id",
        "name",
    )
    search_fields = ("name",)
    date_hierarchy = "created_at"


class IncomeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "amount",
        "category",
        "comment",
        "created_by",
        "wallet",
        "group",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "category",
        "created_by",
        "wallet",
        "group",
        "id",
        "amount",
        "comment",
    )
    date_hierarchy = "created_at"


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "amount",
        "category",
        "comment",
        "created_by",
        "wallet",
        "group",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "category",
        "created_by",
        "wallet",
        "group",
        "id",
        "amount",
        "comment",
    )
    date_hierarchy = "created_at"


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


class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("id", "created_at", "updated_at", "code", "name")
    list_filter = ("created_at", "updated_at", "id", "code", "name")
    search_fields = ("name",)
    date_hierarchy = "created_at"


class CurrencyRateAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "created_at",
        "updated_at",
        "source_currency",
        "target_currency",
        "rate",
    )
    list_filter = (
        "created_at",
        "updated_at",
        "source_currency",
        "target_currency",
        "id",
        "rate",
    )
    date_hierarchy = "created_at"


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)
_register(models.Group, GroupAdmin)
_register(models.Wallet, WalletAdmin)
_register(models.IncomeCategory, IncomeCategoryAdmin)
_register(models.ExpenseCategory, ExpenseCategoryAdmin)
_register(models.Income, IncomeAdmin)
_register(models.Expense, ExpenseAdmin)
_register(models.Transfer, TransferAdmin)
_register(models.Currency, CurrencyAdmin)
_register(models.CurrencyRate, CurrencyRateAdmin)
