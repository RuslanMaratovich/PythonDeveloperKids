from random import randint

import pygame as pg

size = (500, 500)
screen = pg.display.set_mode(size)  # Открыть окно с размерами size

fps = 2

clock = pg.time.Clock() # создаем объект clock класса Clock


while True:
    r = randint(0, 255)
    screen.fill(pg.Color(r, 110, 110))  # задать цвет окна

    type = randint(0,3)
    if type == 0:
        # pg.draw.circle(screen, color, (centerx, centery), radius) — функциядля отрисовки окружности.
        pg.draw.circle(screen, pg.Color("red"), (100, 100), 50)
    if type == 1:
        # pg.draw.rect(screen, color, (x, y, width, height)) функция для отрисовки закрашенного прямоугольника.
        # pg.draw.rect(screen, color, (x, y, width, height), circuit) функция для отрисовки не закрашенного прямоугольника.
        pg.draw.rect(screen, pg.Color("blue"), (200, 300, 70, 100), 20)
    if type == 2:
        # pg.draw.ellipse(screen, color, (x, y, width, height)) — функция для отрисовки овала.
        pg.draw.ellipse(screen, pg.Color("green"), (178, 20, 70, 100))
    if type == 3:
        # pg.draw.polygon(screen, color, ((x, y), (x, y), (x, y))) — функция для отрисовки многоугольника.
        pg.draw.polygon(screen, pg.Color("black"), ((150, 170), (450, 70), (30, 20)))

    pg.display.flip() # отрисовка экрана
    clock.tick(fps) # задержка кадров в секунду

