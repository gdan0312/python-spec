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


class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    def __mul__(self, k):
        return self.x * k, self.y * k

    def __len__(self):
        return int(math.sqrt(self.x * self.x + self.y * self.y))

    def int_pair(self):
        return int(self.x), int(self.y)


class Polyline:
    def __init__(self):
        self.points = []
        self.speeds = []

    def add_point(self, pos: Tuple[float, float]) -> None:
        """
        Добавление в ломанную точки с ее координатами и скоростью
        """
        self.points.append(Vec2d(x=pos[0], y=pos[1]))
        self.speeds.append((random.random() * 2, random.random() * 2))

    def draw_points(self, display, style='points', width=3):
        """
        Отрисовка точек на экране
        """
        pass


class Knot(Polyline):
    def __init__(self):
        super().__init__()
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

    def run(self):
        while self.__working:
            for event in pygame.event.get():
                self.__event_handler(event)

            pygame.display.flip()

        pygame.display.quit()
        pygame.quit()
        exit(0)

    def __event_handler(self, event) -> None:
        """
        Обработка события нажатия клавиши на клавитатуре или щелчка мыши
        """
        if event.type == pygame.QUIT:
            self.__quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.__quit()
            if event.key == pygame.K_PLUS:
                self.__steps += 1
            if event.key == pygame.K_MINUS:
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
        font1 = pygame.font.SysFont(name='courier', size=24)
        font2 = pygame.font.SysFont(name='serif', size=24)


if __name__ == '__main__':
    screen = Screen()
    screen.run()
