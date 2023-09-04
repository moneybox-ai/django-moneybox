from clients.currency.cbrclient import cbr_klient
from moneybox.celery import app
from wallet.models.currency import Currency


@app.task
def get_exchange_rates():
    """Delivering valute courses from cbr.ru."""
    currencies = cbr_klient.get_currencies_rates()
    for code, code_data in currencies.items():
        is_present = Currency.objects.filter(code=code).exists()
        if is_present:
            Currency.objects.filter(code=code).update(
                nominal=code_data.get("Nominal", "No nominal"),
                value=code_data.get("Value", "No value")
            )
        else:
            Currency.objects.update_or_create(
                code=code,
                name=code_data.get("Name", code),
                nominal=code_data.get("Nominal", "No nominal"),
                value=code_data.get("Value", "No value"),
                #TODO etit updated_at field
                updated_at="no field"
                
            )
