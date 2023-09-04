from clients.currency.cbrclient import cbr_klient
from moneybox.celery import app


@app.task
def get_exchange_rates():
    """Delivering valute courses from cbr.ru."""
    return cbr_klient.get_currencies_rates()
