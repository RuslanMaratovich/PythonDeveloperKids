'''прямоугольник'''

import pygame as pg

size = (500, 500)
screen = pg.display.set_mode(size)  # Открыть окно с размерами size

fps = 2

clock = pg.time.Clock()  # создаем объект clock класса Clock

small_rect = pg.Rect(200, 300, 70, 100) # создаем объект small_rect класса Rect с данными для прямоугольника

while True:
    screen.fill(pg.Color(255, 255, 255))  # задать цвет окна

    # pg.draw.rect(screen, color, (x, y, width, height)) функция для отрисовки закрашенного прямоугольника.
    # pg.draw.rect(screen, color, (x, y, width, height), circuit) функция для отрисовки не закрашенного прямоугольника.
    pg.draw.rect(screen, pg.Color("blue"), small_rect, 20)

    pg.display.flip()  # отрисовка экрана
    clock.tick(fps)  # задержка кадров в секунду
