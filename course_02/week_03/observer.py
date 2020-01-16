"""
Пример реализации паттерна наблюдатель
"""

from abc import ABC, abstractmethod


class Engine:
    pass


class ObservableEngine(Engine):
    def __init__(self):
        self.subscribers = set()

    def subscribe(self, subscriber):
        self.subscribers.add(subscriber)

    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)

    def notify(self, achievement):
        for subscriber in self.subscribers:
            subscriber.update(achievement)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achievement):
        raise NotImplementedError


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()

    def update(self, achievement):
        self.achievements.add(achievement['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, achievement):
        if achievement not in self.achievements:
            self.achievements.append(achievement)


if __name__ == '__main__':
    achievement = {"title": "Покоритель", "text": "Дается при выполнении всех заданий в игре"}
    printer1 = ShortNotificationPrinter()
    printer2 = FullNotificationPrinter()
    engine = ObservableEngine()
    engine.subscribe(printer1)
    engine.subscribe(printer2)
    engine.notify(achievement)
    print(printer1.achievements)
