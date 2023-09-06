from clients.currency.cbrclient import cbr_сlient
from moneybox.celery import app
from wallet.models.currency import Currency


@app.task
def get_exchange_rates():
    """Delivering valute courses from cbr.ru."""
    def create_or_update_table_currency(currencies):
        for code, code_data in currencies.items():
            Currency.objects.update_or_create(
                code=code,
                name=code_data.get("name", code),
                )  

    currencies = cbr_сlient.get_currencies_rates()
    create_or_update_table_currency(currencies)
