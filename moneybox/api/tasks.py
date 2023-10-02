from django.utils import timezone

from clients.currency.cbr.cbr import cbr_client
from clients.currency.coingecko.coingecko import coingecko_client
from moneybox.celery import app
from wallet.models.currency import Currency, CurrencyRate, CurrencyType
from wallet.models.invite import Invite


@app.task
def get_exchange_rates():
    """Delivering currency rates from cbr.ru"""
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


@app.task
def update_crypto_exchange_rates():
    """Delivering cryptocurrency rates from coingecko.com"""
    rates = coingecko_client.get_rates()
    for currency, rate in rates.items():
        currency, _ = Currency.objects.get_or_create(
            code=currency.upper()[:4],
            name=currency,
            type=CurrencyType.CRYPTO,
        )
        CurrencyRate.objects.create(currency=currency, rate=round(rate, 4))
