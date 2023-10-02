import requests

from clients.currency.coingecko.defs import CoinGeckoCrypto
from clients.currency.coingecko.exceptions import CoinGeckoRequestException
from moneybox.settings import COINGECKO_URL, COINGECKO_TIMEOUT
from wallet.models.currency import FiatCurrency


class CoinGeckoClient:
    def __init__(self, url: str = COINGECKO_URL, timeout: int = COINGECKO_TIMEOUT) -> None:
        self.url = url
        self.timeout = timeout

    def get_rates(self):
        try:
            response = requests.get(
                url=self.url.format(
                    crypto_currencies=",".join(CoinGeckoCrypto.map_main_crypto_to_coingecko().values()),
                    fiat_currency=FiatCurrency.RUB,
                ),
                timeout=self.timeout,
            )
            rates = response.json()
        except requests.exceptions.RequestException as e:
            raise CoinGeckoRequestException(e)
        result = dict()
        for k, v in rates.items():
            result[CoinGeckoCrypto.map_coingecko_to_main_crypto(k)] = round(v.get(FiatCurrency.RUB.lower()), 4)
        return result


coingecko_client = CoinGeckoClient()
