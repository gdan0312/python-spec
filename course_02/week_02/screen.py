import math
import random
from typing import Tuple

import pygame

SCREEN_DIM = (800, 600)


class Color:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    WET_ASPHALT = (50, 50, 50)
    PURPLE = (128, 128, 255)
    RED = (255, 50, 50, 255)


class Vec2d:
    """
    Класс двумерного вектора
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Сумма векторов
        """
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        """
        Разность векторов
        """
        return self.x - other.x, self.y - other.y

    def __mul__(self, k):
        """
        Умножение вектора на число
        """
        return self.x * k, self.y * k

    def __len__(self):
        """
        Длина вектора
        """
        return int(math.sqrt(self.x * self.x + self.y * self.y))

    def int_pair(self) -> Tuple[int, int]:
        """
        Получение текущих координат вектора
        :return: кортеж из двух целых чисел - координат вектора
        """
        return int(self.x), int(self.y)


class Polyline:
    """
    Класс ломаной линии
    """
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, pos: Tuple[float, float]) -> None:
        """
        Добавление в ломаную точки с ее координатами и скоростью
        """
        self.points.append(Vec2d(x=pos[0], y=pos[1]))
        self.speeds.append((random.random() * 2, random.random() * 2))

    def set_points(self) -> None:
        """
        Перерасчет координат опорных точек
        """
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p][0] > SCREEN_DIM[0] or self.points[p][0] < 0:
                self.speeds[p] = (-self.speeds[p][0], self.speeds[p][1])
            if self.points[p][1] > SCREEN_DIM[1] or self.points[p][1] < 0:
                self.speeds[p] = (self.speeds[p][0], -self.speeds[p][1])

    def draw_points(self, display, style='points', width=3) -> None:
        """
        Отрисовка точек на экране
        """
        if style == 'line':
            for p_n in range(-1, len(self.points) - 1):
                pygame.draw.line(display,
                                 Color.WHITE,
                                 self.points[p_n].int_pair(),
                                 self.points[p_n + 1].int_pair(),
                                 width)
        else:
            for p in self.points:
                pygame.draw.circle(display, Color.WHITE, p.int_pair(), width)


class Knot(Polyline):
    def __init__(self):
        super().__init__()

    def get_knot(self, count):
        pass


class Screen:
    def __init__(self):
        pygame.init()
        self.__display = pygame.display.set_mode(SCREEN_DIM)
        pygame.display.set_caption('MyScreenSaver')
        self.__pause = True
        self.__show_help = False
        self.__working = True
        self.__steps = 35
        self.__knot = Knot()

    def run(self) -> None:
        """
        Запуск программы
        """
        while self.__working:
            for event in pygame.event.get():
                self.__event_handler(event)
            if self.__show_help:
                self.__draw_help()

            self.__knot.draw_points(self.__display)

            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()
        exit(0)

    def __event_handler(self, event) -> None:
        """
        Обработка события нажатия клавиши на клавиатуре или щелчка мыши
        """
        if event.type == pygame.QUIT:
            self.__quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__quit()
            if event.key == pygame.K_KP_PLUS:
                self.__steps += 1
            if event.key == pygame.K_KP_MINUS:
                self.__steps -= 1 if self.__steps > 1 else 0
            if event.key == pygame.K_r:
                self.__knot.points = []
                self.__knot.speeds = []
            if event.key == pygame.K_F1:
                self.__show_help = not self.__show_help
            if event.key == pygame.K_p:
                self.__pause = not self.__pause

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.__knot.add_point(event.pos)

    def __quit(self) -> None:
        """
        Завершение работы программы
        """
        self.__working = False

    def __draw_help(self) -> None:
        """
        Отрисовка окна справки программы
        """
        self.__display.fill(Color.WET_ASPHALT)
        font1 = pygame.font.SysFont('courier', 24)
        font2 = pygame.font.SysFont('serif', 24)
        data = [
            ['F1', 'Show help'],
            ['R', 'Restart'],
            ['P', 'Pause/Play'],
            ['Num+', 'More points'],
            ['Num-', 'Less points'],
            ['', ''],
            [str(self.__steps), 'Current points']
        ]
        #  рисуем красную рамку вокруг экрана
        coords = [(0, 0), (SCREEN_DIM[0], 0), (SCREEN_DIM[0], SCREEN_DIM[1]), (0, SCREEN_DIM[1])]
        pygame.draw.lines(self.__display, Color.RED, True, coords, 5)
        #  выводим текст окна помощи
        for i, text in enumerate(data):
            self.__display.blit(font1.render(text[0], True, Color.PURPLE), (100, 100 + 30 * i))
            self.__display.blit(font2.render(text[1], True, Color.PURPLE), (200, 100 + 30 * i))


if __name__ == '__main__':
    screen = Screen()
    screen.run()
