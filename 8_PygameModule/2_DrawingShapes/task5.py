'''Линия'''

import pygame as pg


def draw_signals(screen):
    pg.draw.circle(screen, pg.Color("yellow"), (400, 400), 300)
    pg.draw.circle(screen, pg.Color("orange"), (500, 150), 20)
    pg.draw.circle(screen, pg.Color("orange"), (600, 340), 60)
    pg.draw.circle(screen, pg.Color("orange"), (200, 500), 60)
    pg.draw.circle(screen, pg.Color("orange"), (400, 370), 20)
    pg.draw.circle(screen, pg.Color("orange"), (300, 200), 50)
    pg.draw.circle(screen, pg.Color("orange"), (500, 640), 20)

    return screen


size = (500, 500)

screen = pg.display.set_mode(size)  # Открыть окно с размерами size

fps = 2

clock = pg.time.Clock()  # создаем объект clock класса Clock

small_rect = pg.Rect(200, 300, 70, 100)  # создаем объект small_rect класса Rect с данными для прямоугольника

while True:
    screen.fill(pg.Color(255, 255, 255))  # задать цвет окна

    draw_signals(screen)

    pg.display.flip()  # отрисовка экрана
    clock.tick(fps)  # задержка кадров в секунду
