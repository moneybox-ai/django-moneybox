# vim: set fileencoding=utf-8 :
from django.contrib import admin

from users.models import Profile
<<<<<<< HEAD
from wallet.admin import *
=======
from wallet.admin import (
    ProfileAdmin,
    GroupAdmin,
    WalletAdmin,
    IncomeCategoryAdmin,
    ExpenseCategoryAdmin,
    IncomeAdmin,
    ExpenseAdmin,
    TransferAdmin,
    CurrencyAdmin,
    CurrencyRateAdmin,
)
>>>>>>> upstream/main
from wallet.models.currency import Currency, CurrencyRate
from wallet.models.expense import ExpenseCategory, Expense
from wallet.models.group import Group
from wallet.models.income import IncomeCategory, Income
from wallet.models.transfer import Transfer
from wallet.models.wallet import Wallet


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
