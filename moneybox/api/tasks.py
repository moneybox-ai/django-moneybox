from moneybox.celery import app
from clients.currency.cbrclient import CBRClient


@app.task
def get_CBR_valute_kurs():
    cbr_klient = CBRClient()
    #print(cbr_klient.cbr_kurs_date)
    return cbr_klient.get_currencies_rates()
