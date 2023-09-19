'''Линия'''

import pygame as pg

size = (500, 500)
screen = pg.display.set_mode(size)  # Открыть окно с размерами size

fps = 2

clock = pg.time.Clock()  # создаем объект clock класса Clock

small_rect = pg.Rect(200, 300, 70, 100) # создаем объект small_rect класса Rect с данными для прямоугольника

while True:
    screen.fill(pg.Color(255, 255, 255))  # задать цвет окна

    # pg.draw.line(screen, color, (startx, starty), (finishx, finishy), width) — функция для отрисовки линии.
    pg.draw.line(screen, 'red', (100, 100), (450, 450), 5)

    pg.display.flip()  # отрисовка экрана
    clock.tick(fps)  # задержка кадров в секунду
