from clients.currency.cbrclient import CBRClient
from moneybox.celery import app


@app.task
def get_CBR_valute_kurs():
    """Delivering valute courses from cbr.ru."""
    cbr_klient = CBRClient()
    return cbr_klient.get_currencies_rates()
