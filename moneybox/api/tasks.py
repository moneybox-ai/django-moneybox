from clients.currency.cbrclient import cbr_сlient
from moneybox.celery import app
from wallet.models.currency import Currency, CurrencyRate


def create_or_update_table_currency(currencies):
    for code, code_data in currencies.items():
        Currency.objects.update_or_create(
            code=code,
            name=code_data.get("name", code),
        )
        CurrencyRate.objects.create(
            currency=Currency.objects.get(code=code),
            rate=float(code_data.get("value").replace(",", ".")) / float(code_data.get("nominal")),
        )


@app.task
def get_exchange_rates():
    """Delivering valute courses from cbr.ru."""
    currencies = cbr_сlient.get_currencies_rates()
    create_or_update_table_currency(currencies)
