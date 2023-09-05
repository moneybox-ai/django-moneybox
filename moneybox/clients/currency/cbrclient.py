import requests
from datetime import date
import xml.etree.ElementTree as ET
from moneybox.settings import CBR_TIMEOUT, CBR_URL


class CBRClient:
    def __init__(self, url: str, timeout: int) -> None:
        self.url = url
        self.timeout = timeout

    def get_currencies_rates(self):

        currencies = {
            "RUB": {
                "num_code": "643",
                "char_code": "RUB",
                "nominal": "1",
                "name": "Российский рубль",
                "value": "1"
                }
            }
        current_date = date.today().strftime("%d/%m/%Y")

        try:
            response = requests.get(url=self.url+"?date_req="+current_date, timeout=self.timeout)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        root = ET.fromstring(response.text)
        for valute in root:
            valute_name = valute.find("CharCode").text
            valute_data = {
                "num_code": valute.find("NumCode").text,
                "char_code": valute.find("CharCode").text,
                "nominal": valute.find("Nominal").text,
                "name": valute.find("Name").text,
                "value": valute.find("Value").text
            }
            currencies.setdefault(valute_name, valute_data)
        return currencies


cbr_сlient = CBRClient(url=CBR_URL, timeout=CBR_TIMEOUT)
