from clients.currency.cbrclient import cbr_сlient
from moneybox.celery import app
from wallet.models.currency import Currency


@app.task
def get_exchange_rates():
    """Delivering valute courses from cbr.ru."""
    currencies = cbr_сlient.get_currencies_rates()
    for code, code_data in currencies.items():
        is_present = Currency.objects.filter(code=code).exists()
        if is_present:
            Currency.objects.filter(code=code).update(
                nominal=code_data.get("nominal", "No nominal"),
                value=code_data.get("value", "No value")
            )
        else:
            Currency.objects.update_or_create(
                code=code,
                name=code_data.get("name", code),
                nominal=code_data.get("nominal", "No nominal"),
                value=code_data.get("value", "No value"),
                cbr_valute_id=code_data.get("cbr_valute_id", "No id")
                #TODO edit updated_at field
                #updated_at="no field"
            )
