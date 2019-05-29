"""
Пример программы на использование магических методов __getitem__ и __setitem__
"""


class PascalList:
    """
    В языке программирования Pascal, в отличие от Python, нумерация элементов последовательности начинается с
    единицы. Данный класс имитирует поведение списков в Паскале
    """
    def __init__(self, original_list=None):
        self.container = original_list or []

    def __getitem__(self, item):
        return self.container[item-1]

    def __setitem__(self, key, value):
        self.container[key-1] = value

    def __str__(self):
        return self.container.__str__()


if __name__ == '__main__':
    numbers = PascalList([1, 2, 3, 4, 5])
    print(numbers[1])
    numbers[5] = 25
    print(numbers)
