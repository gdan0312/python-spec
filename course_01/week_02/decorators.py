"""
Пример программы с использованием декораторов
"""

import functools


def logger(func):
    """
    Декоратор, записывающий результат работы функции в файл
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        with open('log.txt', 'w') as f:
            f.write(str(result))
        return result
    return wrapped


@logger
def summator(num_list):
    return sum(num_list)


print('Summator: {}'.format(summator([1, 2, 3, 4])))
print(summator.__name__)
