"""
Пример обработки исключений
"""

import argparse

import requests

parser = argparse.ArgumentParser()
parser.add_argument('--url', dest='url', type=str, required=True)
args = parser.parse_args()

try:
    response = requests.get(args.url, timeout=30)
    response.raise_for_status()
except requests.Timeout:
    print('ошибка timeout, url:', args.url)
except requests.HTTPError as e:
    code = e.response.status_code
    print('ошибка url: {url}, code: {code}'.format(url=args.url, code=code))
except requests.RequestException:
    print('ошибка скачивания url:', args.url)
else:
    print(response.content)
