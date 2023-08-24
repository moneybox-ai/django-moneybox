# vim: set fileencoding=utf-8 :
from django.contrib import admin
import wallet.models as models
import users.models as users_models
from wallet.admin.currency_admin import CurrencyAdmin, CurrencyRateAdmin
from wallet.admin.expense_admin import ExpenseCategoryAdmin, ExpenseAdmin
from wallet.admin.group_admin import GroupAdmin
from wallet.admin.income_admin import IncomeCategoryAdmin, IncomeAdmin
from wallet.admin.profile_admin import ProfileAdmin
from wallet.admin.transfer_admin import TransferAdmin
from wallet.admin.wallet_admin import WalletAdmin


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(users_models.Profile, ProfileAdmin)
_register(models.Group, GroupAdmin)
_register(models.Wallet, WalletAdmin)
_register(models.IncomeCategory, IncomeCategoryAdmin)
_register(models.ExpenseCategory, ExpenseCategoryAdmin)
_register(models.Income, IncomeAdmin)
_register(models.Expense, ExpenseAdmin)
_register(models.Transfer, TransferAdmin)
_register(models.Currency, CurrencyAdmin)
_register(models.CurrencyRate, CurrencyRateAdmin)
