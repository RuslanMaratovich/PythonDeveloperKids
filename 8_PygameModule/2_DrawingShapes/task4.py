'''Смайлик'''

import pygame as pg

size = (500, 500)
screen = pg.display.set_mode(size)  # Открыть окно с размерами size

fps = 2
clock = pg.time.Clock()  # создаем объект clock класса Clock


while True:
    screen.fill(pg.Color(255, 255, 255))  # задать цвет окна

    pg.draw.rect(screen, pg.Color("red"), (50, 50, 400, 400))

    pg.draw.rect(screen, pg.Color("white"), (150, 150, 50, 100))
    pg.draw.rect(screen, pg.Color("white"), (350, 150, 50, 100))

    pg.draw.line(screen, 'white', (150, 300), (250, 350), 4)
    pg.draw.line(screen, 'white', (250, 350), (350, 300), 4)

    pg.display.flip()  # отрисовка экрана
    clock.tick(fps)  # задержка кадров в секунду