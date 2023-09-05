import requests
from datetime import date
import xml.etree.ElementTree as ET


class CBRClient:
    def __init__(self, url: str, timeout: int) -> None:
        self.url = url
        self.timeout = timeout

    def get_currencies_rates(self):

        currencies = {
            "RUB": {
                "NumCode": "643",
                "CharCode": "RUB",
                "Nominal": "1",
                "Name": "Российский рубль",
                "Value": "1"
                }
            }

        try:
            response = requests.get(url=self.url, timeout=self.timeout)
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

        root = ET.fromstring(response.text)
        for valute in root:
            valute_name = valute.find("CharCode").text
            valute_data = {
                "NumCode": valute.find("NumCode").text,
                "CharCode": valute.find("CharCode").text,
                "Nominal": valute.find("Nominal").text,
                "Name": valute.find("Name").text,
                "Value": valute.find("Value").text
            }
            currencies.setdefault(valute_name, valute_data)
        return currencies


current_date = date.today().strftime("%d/%m/%Y")
url = f"https://cbr.ru/scripts/XML_daily.asp?date_req={current_date}"
timeout = 10

cbr_klient = CBRClient(url, timeout)
