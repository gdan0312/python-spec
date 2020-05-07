from decimal import Decimal

from bs4 import BeautifulSoup

URL = 'https://cbr.ru/scripts/XML_daily.asp'


def convert(amount, cur_from, cur_to, date, requests):
    resp = requests.get(URL, params={'date_req': date})
    soup = BeautifulSoup(resp.content, 'xml')
    value_from = _get_value(cur_from, soup)
    rub = value_from * amount
    value_to = _get_value(cur_to, soup)
    end = rub / value_to
    return end.quantize(Decimal('.0001'))


def _get_value(char_code, soup_obj):
    currency = soup_obj.find('CharCode', text=char_code)
    nominal = Decimal(currency.find_next_sibling('Nominal').string)
    value = Decimal(currency.find_next_sibling('Value').string.replace(',', '.'))
    return value / nominal
