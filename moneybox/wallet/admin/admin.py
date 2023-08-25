# vim: set fileencoding=utf-8 :
from django.contrib import admin

from users.models import Profile
from wallet.admin import *
from wallet.models.currency_models import Currency, CurrencyRate
from wallet.models.expense_models import ExpenseCategory, Expense
from wallet.models.group_models import Group
from wallet.models.income_models import IncomeCategory, Income
from wallet.models.transfer_models import Transfer
from wallet.models.wallet_models import Wallet


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(Profile, ProfileAdmin)
_register(Group, GroupAdmin)
_register(Wallet, WalletAdmin)
_register(IncomeCategory, IncomeCategoryAdmin)
_register(ExpenseCategory, ExpenseCategoryAdmin)
_register(Income, IncomeAdmin)
_register(Expense, ExpenseAdmin)
_register(Transfer, TransferAdmin)
_register(Currency, CurrencyAdmin)
_register(CurrencyRate, CurrencyRateAdmin)
