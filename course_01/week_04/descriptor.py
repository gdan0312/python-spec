class Value:
    """
    Пример дескриптора вычитающего комиссию из платежа
    """
    def __init__(self):
        self.amount = 0

    def __get__(self, instance, owner):
        return self.amount

    def __set__(self, instance, value):
        self.amount = value - instance.commission * value


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


if __name__ == '__main__':
    account = Account(0.1)
    account.amount = 100
    print(account.amount)

