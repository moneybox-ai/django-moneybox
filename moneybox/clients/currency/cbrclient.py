import requests
from datetime import date, datetime
import xml.etree.ElementTree as ET


class CBRClient:
    def __init__(self):
        self.cbr_kurs_date, self.cbr_kurs = None, None
        self.get_currencies_rates()

    def get_currencies_rates(self):

        try:
            currencies = {
                'RUB': {
                    'NumCode': '643',
                    'CharCode': 'RUB',
                    'Nominal': '1',
                    'Name': 'Российский рубль',
                    'Value': '1'
                    }
                }

            current_date = date.today().strftime('%d/%m/%Y')
            url = f'https://cbr.ru/scripts/XML_daily.asp?date_req={current_date}'
            response = requests.get(url=url)

            root = ET.fromstring(response.text)

            kurs_date = root.attrib.get('Date', None)
            if kurs_date:
                cbr_kurs_date = datetime.strptime(kurs_date, '%d.%m.%Y').date()

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
                self.cbr_kurs_date, self.currencies = cbr_kurs_date, currencies
                return self.currencies

        except ValueError:
            return None


cbr_klient = CBRClient()
