import json
import functools


def to_json(func):
    """
    Декоратор, преобразующий результат работы функции в json формат
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        return json.dumps(result)
    return wrapped
