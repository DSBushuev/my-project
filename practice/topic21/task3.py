from random import randint

import pygame

from topic21.Class.ball import Ball
from topic21.Class.vector import Vector

pygame.init()

sc = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
WHITE = (200, 200, 200)
RANDOM_COLOR = (randint(0, 255), randint(0, 255), randint(0, 255))
RED = (255, 20, 10)
BlACK = (0, 0, 0)
START_SPEED = (20, 20)
FPS = 30
control_ball = None

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

    keys = pygame.key.get_pressed()
    if control_ball:
        if keys[pygame.K_UP]:
            control_ball.speed.y -= 1
        elif keys[pygame.K_DOWN]:
            control_ball.speed.y += 1
        if keys[pygame.K_RIGHT]:
            control_ball.speed.x += 1
        elif keys[pygame.K_LEFT]:
            control_ball.speed.x -= 1
        elif keys[pygame.K_SPACE]:
            control_ball.speed = Vector(0, 0)
        if keys[pygame.K_b]:
            control_ball.radius += 1
        elif keys[pygame.K_s]:
            control_ball.radius -= 1

    sc.fill(WHITE)

    for n, ball in enumerate(Ball.get_all_ball()):
        if (CURSOR_POS[0] - ball.radius < ball.pos.x < CURSOR_POS[0] + ball.radius) and \
                (CURSOR_POS[1] - ball.radius < ball.pos.y < CURSOR_POS[1] + ball.radius):
            flag_for_new_ball = False
            control_ball = ball
            ball.color = RANDOM_COLOR
            ball.speed = Vector(0, 0)
        for i in range(n + 1, len(Ball.get_all_ball())):
            if ball.clash(Ball.get_all_ball()[i]):
                ball.push_off(Ball.get_all_ball()[i])
        ball.update()
        ball.render()
        ball.speed *= 0.99


    def add_ball(pos):
        Ball(sc, pos, (250,250,250), 20, RANDOM_SPEED)


    if flag_for_new_ball:
        add_ball(CURSOR_POS)

    pygame.display.update()

    clock.tick(FPS)
