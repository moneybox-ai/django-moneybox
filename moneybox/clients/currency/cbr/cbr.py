from .exceptions import CBRRequestException
import requests
from datetime import date
import xml.etree.ElementTree as ET
from moneybox.settings import CBR_TIMEOUT, CBR_URL


class CBRClient:
    def __init__(self, url: str = CBR_URL, timeout: int = CBR_TIMEOUT) -> None:
        self.url = url
        self.timeout = timeout

    def get_currencies_rates(self, target_date=None):
        """Target_date must be str in dd/mm/YYYY format. Example 01/01/2000."""

        currencies = {}

        if target_date is None:
            target_date = date.today().strftime("%d/%m/%Y")

        try:
            response = requests.get(url=self.url + "?date_req=" + target_date, timeout=self.timeout)
        except requests.exceptions.RequestException as e:
            raise CBRRequestException(e)

        root = ET.fromstring(response.text)
        for currency in root:
            valute_name = currency.find("CharCode").text
            valute_data = {
                "num_code": currency.find("NumCode").text,
                "char_code": currency.find("CharCode").text,
                "nominal": float(currency.find("Nominal").text),
                "name": currency.find("Name").text,
                "value": float(currency.find("Value").text.replace(",", ".")),
                "cbr_currency_id": currency.attrib["ID"],
            }
            currencies.setdefault(valute_name, valute_data)
        return currencies


cbr_client = CBRClient()
