from random import randint

import pygame

from topic21.Class.ball import Ball

pygame.init()

sc = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
WHITE = (200, 200, 200)
RANDOM_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
RED = (255, 20, 10)
BlACK = (0, 0, 0)
START_SPEED = (20, 20)
FPS = 30

while 1:
    RANDOM_COLOR = (randint(0, 230), randint(0, 230), randint(0, 230))
    RANDOM_SPEED = (randint(-30, 30), randint(-30, 30))
    CURSOR_POS = (-500, -500)
    flag_for_new_ball = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            CURSOR_POS = event.pos
            flag_for_new_ball = True

    sc.fill(WHITE)

    for ball in Ball.get_all_ball():
        if (CURSOR_POS[0] - 2 * ball.radius < ball.pos.x < CURSOR_POS[0] + 2 * ball.radius) and \
                (ball.pos.y > CURSOR_POS[1] - 2 * ball.radius < CURSOR_POS[1] + 2 * ball.radius):
            flag_for_new_ball = False
            ball.color = RANDOM_COLOR
        ball.update()
        ball.render()


    def add_ball(pos):
        Ball(sc, pos, (250,250,250), 30, RANDOM_SPEED)


    if flag_for_new_ball:
        add_ball(CURSOR_POS)

    pygame.display.update()

    clock.tick(FPS)
