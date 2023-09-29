from django.utils import timezone

from clients.currency.cbrclient import cbr_client
from moneybox.celery import app
from wallet.models.currency import Currency, CurrencyRate
from wallet.models.invite import Invite


@app.task
def get_exchange_rates():
    """Delivering currency courses from cbr.ru"""
    currencies = cbr_client.get_currencies_rates()
    for code, code_data in currencies.items():
        currency, _ = Currency.objects.get_or_create(
            code=code,
            name=code_data.get("name", code),
        )
        rate = code_data.get("value") / code_data.get("nominal")
        CurrencyRate.objects.create(currency=currency, rate=rate)


@app.task
def delete_expired_invites():
    """Removes expired invites"""
    expired_invite_codes = Invite.objects.filter(expires_at__lt=timezone.now())
    expired_invite_codes.delete()
