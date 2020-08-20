"""
Реализация паттерна Цепочка обязанностей
"""

E_INT, E_FLOAT, E_STR = int, float, str


class SomeObject:
    def __init__(self):
        self.integer_field = 0
        self.float_field = 0.0
        self.string_field = ''


class EventGet:
    def __init__(self, kind):
        self.kind = kind


class EventSet:
    def __init__(self, value):
        self.value = value
        self.kind = type(value)


class NullHandler:
    def __init__(self, processor=None):
        self.__processor = processor

    def handle(self, obj, event):
        if self.__processor:
            return self.__processor.handle(obj, event)


class IntHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_INT:
            if isinstance(event, EventGet):
                return obj.integer_field
            obj.integer_field = event.value
        else:
            print('Передаю обработку дальше')
            return super().handle(obj, event)


class FloatHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_FLOAT:
            if isinstance(event, EventGet):
                return obj.float_field
            obj.float_field = event.value
        else:
            print('Передаю обработку дальше')
            return super().handle(obj, event)


class StrHandler(NullHandler):
    def handle(self, obj, event):
        if event.kind == E_STR:
            if isinstance(event, EventGet):
                return obj.string_field
            obj.string_field = event.value
        else:
            print('Передаю обработку дальше')
            return super().handle(obj, event)


if __name__ == '__main__':
    my_obj = SomeObject()
    my_obj.integer_field = 42
    my_obj.float_field = 3.14
    my_obj.string_field = 'some text'
    chain = IntHandler(FloatHandler(StrHandler(NullHandler())))

    print(chain.handle(my_obj, EventGet(int)))
    print(chain.handle(my_obj, EventGet(float)))
    print(chain.handle(my_obj, EventGet(str)))

    chain.handle(my_obj, EventSet(100))
    print(chain.handle(my_obj, EventGet(int)))

    chain.handle(my_obj, EventSet(-42))
    print(chain.handle(my_obj, EventGet(int)))

    chain.handle(my_obj, EventSet(0.5))
    print(chain.handle(my_obj, EventGet(float)))

    chain.handle(my_obj, EventSet(-2.9))
    print(chain.handle(my_obj, EventGet(float)))

    chain.handle(my_obj, EventSet('new text'))
    print(chain.handle(my_obj, EventGet(str)))
