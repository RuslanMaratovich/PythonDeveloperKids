from random import randint

import pygame as pg

size = (500, 500)  # создаем переменную в которую записываем кортеж из 2-х чисел
screen = pg.display.set_mode(size)  # Создаёт видимую поверхность изображения на мониторе. Эта поверхность может либо
# покрывать весь экран, либо быть оконной.

fps = 2  # переменная в которую записываем количество кадров

clock = pg.time.Clock()  # создаем объект clock класса Clock

while True:
    r = randint(0, 255)
    screen.fill(pg.Color(r, 100, 100))  # задать цвет окна

    pg.display.flip()  # отрисовка экрана
    clock.tick(fps)  # задержка кадров в секунду
