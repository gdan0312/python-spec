import os
import tempfile


class File:
    """
    Простой класс для работы с файлами
    """
    def __init__(self, path):
        self.path = os.path.abspath(path)
        self.position = 0

    def __add__(self, other):
        new_path = os.path.join(tempfile.gettempdir(), 'new_file.txt')
        new_file = File(new_path)
        new_file.write(self.read() + other.read())
        return new_file

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.path) as f:
            f.seek(self.position)
            line = f.readline()
            if not line:
                self.position = 0
                raise StopIteration
            self.position = f.tell()
            return line

    def read(self):
        with open(self.path) as f:
            return f.read()

    def write(self, s):
        with open(self.path, 'w') as f:
            f.write(s)
