import json
import base64

import requests

HOST = 'https://datasend.webpython.graders.eldf.ru'


def post_request():
    resp = requests.post(url=f'{HOST}/submissions/1/', headers={
        'Authorization': 'Basic YWxsYWRpbjpvcGVuc2VzYW1l'
    })
    try:
        return resp.json()
    except json.JSONDecodeError:
        pass


def put_request(data):
    try:
        login = data['login']
        password = data['password']
        path = data['path']
        resp = requests.put(url=f'{HOST}/{path}', headers={
            'Authorization': f"Basic {base64.b64encode(f'{login}:{password}'.encode()).decode()}"
        })
        return resp.json()
    except (json.JSONDecodeError, KeyError):
        pass


def save(data):
    with open('answer.txt', 'w') as f:
        try:
            f.write(data['answer'])
        except KeyError:
            pass


if __name__ == '__main__':
    instructions = post_request()
    code = put_request(instructions)
    save(code)
