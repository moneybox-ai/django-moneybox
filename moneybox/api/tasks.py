from clients.currency.cbrclient import cbr_klient
from moneybox.celery import app
from wallet.models.currency import Currency


@app.task
def get_exchange_rates():
    """Delivering valute courses from cbr.ru."""
    currencies = cbr_klient.get_currencies_rates()
    for code, code_data in currencies.items():
        Currency.objects.get_or_create(code=code, name=code_data['Name'])
