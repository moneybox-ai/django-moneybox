import requests

from clients.currency.defs import Response

from moneybox.settings import EXCHANGE_RATE_API_CLIENT


class ExchangeRatesAPIClient:
    LATEST = "https://openexchangerates.org/api/latest.json"
    CURRENCIES = "https://openexchangerates.org/api/currencies.json"

    def __init__(self, api_key) -> dict[str, float]:
        self.api_key = api_key

    def get_currencies(self) -> dict[str, str]:
        response = requests.get(
            f"{self.CURRENCIES}?app_id={self.api_key}", timeout=10
        )
        response.raise_for_status()
        return response.json()

    def get_rates(self):
        response = requests.get(
            f"{self.LATEST}?app_id={self.api_key}", timeout=10
        )
        response.raise_for_status()
        resp = Response(**response.json())
        return resp.rates


client = ExchangeRatesAPIClient(api_key=EXCHANGE_RATE_API_CLIENT)
