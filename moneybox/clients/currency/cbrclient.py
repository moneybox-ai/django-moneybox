import requests
from datetime import date, datetime
import xml.etree.ElementTree as ET


class CBRClient:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.cbr_curs_date, self.cbr_curs = self.get_currencies_rates()

    def get_currencies_rates(self):

        try:
            currencies = dict()

            current_date = date.today().strftime('%d/%m/%Y')
            url = f'https://cbr.ru/scripts/XML_daily.asp?date_req={current_date}'
            response = requests.get(url=url)

            root = ET.fromstring(response.text)

            curs_date = root.attrib.get('Date', None)
            if curs_date:
                cbr_curs_date = datetime.strptime(curs_date, '%d.%m.%Y').date()

            for i in range(len(root)):
                currency_dict = dict()
                valute_id = root[i].attrib

                if isinstance(type(valute_id), dict):
                    currency_dict.update(valute_id)

                for item in root[i]:
                    if item.tag and item.text:
                        currency_dict.setdefault(item.tag, item.text)
                currency_name = currency_dict.get('CharCode')
                currencies.setdefault(currency_name, currency_dict)

            if currencies:
                return cbr_curs_date, currencies

        except ValueError:
            return None, None
