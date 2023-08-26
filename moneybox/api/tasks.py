from clients.currency.client import client


def update_currency():
    import django

    django.setup()
    from wallet.models import Currency, CurrencyRate

    usd = Currency.get_usd()
    currencies = client.get_currencies()
    for code, rate in client.get_rates().items():
        target_currency, _ = Currency.objects.get_or_create(code=code, name=currencies[code])
        CurrencyRate.objects.create(source_currency=usd, target_currency=target_currency, rate=rate)
