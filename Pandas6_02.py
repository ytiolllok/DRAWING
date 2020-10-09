import numpy as np
import pygame as pg
from pygame.draw import *

pg.init()

FPS = 30
screen = pg.display.set_mode((800,   600))

"цвет дерева"
tree_color = (0, 200, 64)
"цвет фона"
screen_color = (255, 175, 128)
"черный"
BLACK = (0, 0, 0)
"белый"
WHITE = (255, 255, 255)
"заливка фона"
screen.fill(screen_color)

def log(x, y, scale_fact):
    """
    Функция рисует ствол дерева на экране
    х, y - координаты левого нижнего угла ствола
    scale_fact - размер дерева в условных единицах, толщина основания ствола
    единичного дерева - 16 пикселей
    """
    surface_log = pg.Surface((800, 600))
    
    surface_log.set_colorkey(BLACK)

    rect(screen, tree_color,
         (x, y, 16*scale_fact, 50*scale_fact))
    rect(surface_log, tree_color,
         (x, y - 55*scale_fact, 16*scale_fact, 50*scale_fact))
    rect(surface_log, tree_color,
         (x + 2*scale_fact, y - 80*scale_fact, 10*scale_fact, 20*scale_fact))
    rect(surface_log, tree_color,
         (x + 4*scale_fact, y - 95*scale_fact, 8*scale_fact, 10*scale_fact))

    screen.blit(surface_log, (0, 0))


def leaves(x, y, scale_fact):
    """
    Функция рисует 4 ветки с листьями, которые гармонично смотрятся
    вместе с деревом
    x, y - координаты левого нижнего ствола дерева
    scale_fact - размер веток в условных единицах.
    Он должен совпадать с размером дерева, чтобы картина была сбалансированной
    """
    surface_leaves_R = pg.Surface((800, 600))
    surface_leaves_L = pg.Surface((800, 600))

    surface_leaves_L.set_colorkey(BLACK)
    surface_leaves_R.set_colorkey(BLACK)

    arc(surface_leaves_R, tree_color,
    (x + 20*scale_fact, y - 40*scale_fact, 60*scale_fact, 50*scale_fact),
                    0, np.pi, 2)
    arc(surface_leaves_R, tree_color,
    (x + 20*scale_fact, y - 80*scale_fact, 40*scale_fact, 25*scale_fact),
                    0, np.pi, 2)

    arc(surface_leaves_L, tree_color,
    (x - 65*scale_fact, y - 40*scale_fact, 60*scale_fact, 50*scale_fact),
                    0, np.pi, 2)
    arc(surface_leaves_L, tree_color,
    (x - 45*scale_fact, y - 80*scale_fact, 40*scale_fact, 25*scale_fact),
                    0, np.pi, 2)

    ellipse(surface_leaves_R, tree_color,
       [x + 40*scale_fact, y - 35*scale_fact, 10*scale_fact, 30*scale_fact])
    ellipse(surface_leaves_R, tree_color,
       [x + 50*scale_fact, y - 35*scale_fact, 8*scale_fact, 25*scale_fact])
    ellipse(surface_leaves_R, tree_color,
       [x + 62*scale_fact, y - 32*scale_fact, 6*scale_fact, 20*scale_fact])
    ellipse(surface_leaves_R, tree_color,
       [x + 30*scale_fact, y - 33*scale_fact, 8*scale_fact, 25*scale_fact])

    ellipse(surface_leaves_L, tree_color,
       [x - 24*scale_fact, y - 35*scale_fact, 10*scale_fact, 30*scale_fact])
    ellipse(surface_leaves_L, tree_color,
       [x - 50*scale_fact, y - 35*scale_fact, 8*scale_fact, 25*scale_fact])
    ellipse(surface_leaves_L, tree_color,
       [x - 58*scale_fact, y - 32*scale_fact, 6*scale_fact, 20*scale_fact])
    ellipse(surface_leaves_L, tree_color,
       [x - 36*scale_fact, y - 33*scale_fact, 8*scale_fact, 25*scale_fact])

    ellipse(surface_leaves_R, tree_color,
       [x + 36*scale_fact, y - 77*scale_fact, 8*scale_fact, 20*scale_fact])
    ellipse(surface_leaves_R, tree_color,
       [x + 50*scale_fact, y - 75*scale_fact, 6*scale_fact, 15*scale_fact])
    ellipse(surface_leaves_R, tree_color,
       [x + 26*scale_fact, y - 73*scale_fact, 5*scale_fact, 15*scale_fact])

    ellipse(surface_leaves_L, tree_color,
       [x - 36*scale_fact, y - 77*scale_fact, 8*scale_fact, 20*scale_fact])
    ellipse(surface_leaves_L, tree_color,
       [x - 20*scale_fact, y - 75*scale_fact, 6*scale_fact, 15*scale_fact])
    ellipse(surface_leaves_L, tree_color,
       [x - 26*scale_fact, y - 77*scale_fact, 5*scale_fact, 15*scale_fact])

    screen.blit(surface_leaves_L, (0, 0))
    screen.blit(surface_leaves_R, (0, 0))


def panda(x, y, scale_fact):
    """
    Функция рисует панду
    x, y - координаты шеи панды
    scale_fact - размер панды в условных единицах
    длина туловища единичной панды - 100 пикселей
    """    
    circle(screen, BLACK,
       (x + 24*scale_fact, y - 35*scale_fact), scale_fact*18)
    circle(screen, BLACK,
       (x - 28*scale_fact, y - 33*scale_fact), scale_fact*20)

    rect(screen, BLACK,
       (x - 14*scale_fact, y, 18*scale_fact, 56*scale_fact))

    ellipse(screen, WHITE,
       [x, y, 100*scale_fact, 60*scale_fact])

    rect(screen, BLACK,
       (x + 12*scale_fact, y, 18*scale_fact, 70*scale_fact))

    circle(screen, WHITE,
       (x, y), scale_fact*43)

    rect(screen, BLACK,
       (x - 12*scale_fact, y + 60*scale_fact, 42*scale_fact, 18*scale_fact))

    ellipse(screen, BLACK,
       [x + 80*scale_fact, y + 30*scale_fact, 18*scale_fact, 49*scale_fact])

    circle(screen, BLACK,
       (x - 34*scale_fact, y + 10*scale_fact), scale_fact*11)
    circle(screen, BLACK,
       (x, y + 13*scale_fact), scale_fact*11)
    circle(screen, BLACK,
       (x - 20*scale_fact, y + 32*scale_fact), scale_fact*7)


def palm(x, y, scale_fact):
    """
    Функция рисует ствол дерева на экране
    х, y - координаты левого нижнего угла ствола
    scale_fact - размер дерева в условных единицах, толщина основания ствола
    единичного дерева - 16 пикселей
    """
    log(x, y, scale_fact)
    
    leaves(x, y, scale_fact)

palm(200, 300, 3)
palm(50, 400, 1)
palm(600, 200, 2)

panda(500, 300, 2)
panda(300, 500, 1)

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()

