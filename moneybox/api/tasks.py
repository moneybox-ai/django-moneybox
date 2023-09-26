from django.utils import timezone

from clients.currency.cbrclient import cbr_сlient
from moneybox.celery import app
from wallet.models.currency import Currency, CurrencyRate
from wallet.models.invite import Invite


def create_rates(currency, rate):
    CurrencyRate.objects.create(currency=currency, rate=rate)


def create_or_update_table_currency(currencies):
    for code, code_data in currencies.items():
        Currency.objects.update_or_create(
            code=code,
            name=code_data.get("name", code),
        )
        currency = (Currency.objects.get(code=code),)
        rate = code_data.get("value") / code_data.get("nominal")
        create_rates(currency, rate)


@app.task
def get_exchange_rates():
    """Delivering valute courses from cbr.ru."""
    currencies = cbr_сlient.get_currencies_rates()
    create_or_update_table_currency(currencies)


@app.task
def delete_expired_invites():
    expired_invite_codes = Invite.objects.filter(expires_at__lt=timezone.now())
    expired_invite_codes.delete()
