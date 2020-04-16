"""
Задание по работе с библиотекой requests и api сайта Вконтакте
"""

from datetime import datetime
from json.decoder import JSONDecodeError

import requests


API_URL = 'https://api.vk.com/method'
ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711'
API_VERSION = '5.71'


def calc_age(uid):
    """
    Расчет распределения возрастов друзей пользователя
    :param uid: идентификатор или никнейм пользователя
    :return:
    """
    user_id = get_user_id_by_username(uid)
    if user_id is None:
        return

    friends = get_friends_list(user_id)
    if friends is None:
        return

    current_year = datetime.now().year
    ages = {}

    for friend in friends:
        bdate = friend.get('bdate')
        if bdate is None:
            continue

        bdate = bdate.split('.')
        if len(bdate) != 3:
            continue

        birth_year = int(bdate[2])
        age = current_year - birth_year
        ages.setdefault(age, 0)
        ages[age] += 1

    return sorted(ages.items(), key=lambda x: (-x[1], x[0]))


def get_user_id_by_username(uid):
    """
    Получение идентификатора пользователя по его никнейму
    :param uid: никнейм пользователя
    :return:
    """
    resp = requests.get(f'{API_URL}/users.get', params={
        'access_token': ACCESS_TOKEN,
        'v': API_VERSION,
        'user_ids': uid
    })
    try:
        resp = resp.json()
        resp = resp['response']
        user = resp[0]
        return user['id']
    except (JSONDecodeError, KeyError, IndexError):
        pass


def get_friends_list(user_id):
    """
    Получение списка друзей пользователя
    :param user_id: идентификатор пользователя
    :return:
    """
    resp = requests.get(f'{API_URL}/friends.get', params={
        'access_token': ACCESS_TOKEN,
        'v': API_VERSION,
        'user_id': user_id,
        'fields': 'bdate'
    })
    try:
        resp = resp.json()
        resp = resp['response']
        return resp['items']
    except (JSONDecodeError, KeyError):
        pass


if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
