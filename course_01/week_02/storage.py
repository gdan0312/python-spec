import os
import json
import argparse
import tempfile


class Storage:
    def __init__(self):
        self.storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

    def _get_data(self):
        """
        Получение объекта с данными из файла
        """
        if not os.path.exists(self.storage_path):
            return dict()

        with open(self.storage_path) as f:
            return json.load(f)

    def read(self, key):
        """
        Получение записи из файла по заданному ключу
        :param key: ключ для поиска значения в файле
        :return: список значений по заданному ключу или None в случае отсутствия ключа
        """
        data = self._get_data()
        return data.get(key)

    def write(self, key, value):
        """
        Запись значения в файл по заданному ключу
        :param key: ключ для записи значения в файл
        :param value: значение для записи в файл по данному ключу
        """
        data = self._get_data()
        if key not in data:
            data[key] = [value]
        else:
            data[key].append(value)

        with open(self.storage_path, 'w') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', dest='key')
    parser.add_argument('--value', dest='value')
    args = parser.parse_args()
    storage = Storage()
    if args.key and args.value:
        storage.write(args.key, args.value)
    else:
        print(storage.read(args.key))
