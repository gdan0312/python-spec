import math
import random
from typing import Tuple

import pygame

SCREEN_DIM = (800, 600)


class Color:
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PURPLE = (128, 128, 255)
    WET_ASPHALT = (50, 50, 50)


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
        return Vec2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """
        Разность векторов
        """
        return Vec2d(self.x - other.x, self.y - other.y)

    def __mul__(self, k):
        """
        Умножение вектора на число
        """
        return Vec2d(self.x * k, self.y * k)

    def __len__(self):
        """
        Длина вектороа
        """
        return int(math.sqrt(self.x * self.x + self.y * self.y))

    def int_pair(self) -> Tuple[int, int]:
        """
        Получение текущих координат вектора
        :return: пара целых чисел - текущих координат вектора на экране
        """
        return int(self.x), int(self.y)


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def reset(self) -> None:
        """
        Сброс ломаной
        """
        self.points = []
        self.speeds = []

    def add_point(self, pos) -> None:
        """
        Добавление в ломаную точки с ее скоростью
        :param pos: координаты точки на экране
        """
        self.points.append(Vec2d(pos[0], pos[1]))
        self.speeds.append(Vec2d(random.random() * 2, random.random() * 2))

    def draw_points(self, display, width=3) -> None:
        """
        Отрисовка точек
        :param display: экран программы
        :param width: ширина точки
        """
        for p in self.points:
            pygame.draw.circle(display, Color.WHITE, p.int_pair(), width)

    def set_points(self) -> None:
        """
        Перерасчет координат опорных точек
        """
        for p in range(len(self.points)):
            self.points[p] = self.points[p] + self.speeds[p]
            if self.points[p].x > SCREEN_DIM[0] or self.points[p].x < 0:
                self.speeds[p] = Vec2d(-self.speeds[p].x, self.speeds[p].y)
            if self.points[p].y > SCREEN_DIM[1] or self.points[p].y < 0:
                self.speeds[p] = Vec2d(self.speeds[p].x, -self.speeds[p].y)


class Knot(Polyline):
    def __init__(self):
        super().__init__()
        self.steps = 35
        self.__hue = 0
        self.__color = pygame.Color(0)

    def draw_points(self, display, width=3) -> None:
        """
        Отрисовка ломаной
        :param display: экран программы
        :param width: ширина ломаной
        """
        super().draw_points(display)
        self.__hue = (self.__hue + 1) % 360
        self.__color.hsla = (self.__hue, 100, 50, 100)
        points = self.__get_knot()
        for p_n in range(-1, len(points) - 1):
            pygame.draw.line(display, self.__color, points[p_n].int_pair(), points[p_n + 1].int_pair(), width)

    def __get_knot(self):
        if len(self.points) < 3:
            return []


class Screen:
    def __init__(self):
        pygame.init()
        self.__display = pygame.display.set_mode(SCREEN_DIM)
        pygame.display.set_caption('MyScreenSaver')
        self.__working = True
        self.__pause = True
        self.__show_help = False
        self.__knot = Knot()

    def run(self) -> None:
        """
        Основной метод программы
        """
        while self.__working:
            for event in pygame.event.get():
                self.__event_handler(event)

            self.__display.fill(Color.BLACK)
            self.__knot.draw_points(self.__display)

            if not self.__pause:
                self.__play()

            if self.__show_help:
                self.__draw_help()

            pygame.display.flip()

    def __event_handler(self, event) -> None:
        """
        Обработка событий от пользователя
        :param event: событие от пользователя
        """
        if event.type == pygame.QUIT:
            self.__quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__quit()
            if event.key == pygame.K_r:
                self.__reset()
            if event.key == pygame.K_F1:
                self.__show_help = not self.__show_help
            if event.key == pygame.K_p:
                self.__pause = not self.__pause
            if event.key == pygame.K_KP_PLUS:
                self.__knot.steps += 1
            if event.key == pygame.K_KP_MINUS:
                self.__knot.steps -= 1 if self.__knot.steps > 1 else 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.__knot.add_point(event.pos)

    def __quit(self) -> None:
        """
        Выход из программы
        """
        self.__working = False
        pygame.display.quit()
        pygame.quit()
        exit(0)

    def __reset(self):
        """
        Перезапуск программы
        """
        self.__knot.reset()

    def __play(self) -> None:
        """
        Запуск движения ломаной
        """
        self.__knot.set_points()

    def __draw_help(self) -> None:
        """
        Отрисовка окна помощи
        """
        self.__display.fill(Color.WET_ASPHALT)
        font1 = pygame.font.SysFont('courier', 24)
        font2 = pygame.font.SysFont('serif', 24)
        points = [(0, 0), (SCREEN_DIM[0], 0), (SCREEN_DIM[0], SCREEN_DIM[1]), (0, SCREEN_DIM[1])]
        data = [
            ['F1', 'Show Help'],
            ['R', 'Restart'],
            ['P', 'Pause/Play'],
            ['Num+', 'More points'],
            ['Num-', 'Less points'],
            ['', ''],
            [str(self.__knot.steps), 'Current points'],
        ]
        # рисуем красную рамку во внутренней части окна
        pygame.draw.lines(self.__display, Color.RED, True, points, 5)
        # выводим текст окна помощи
        for i, text in enumerate(data):
            self.__display.blit(font1.render(text[0], True, Color.PURPLE), (100, 100 + 30 * i))
            self.__display.blit(font2.render(text[1], True, Color.PURPLE), (200, 100 + 30 * i))


if __name__ == '__main__':
    screen = Screen()
    screen.run()
