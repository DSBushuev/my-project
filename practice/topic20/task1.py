import pygame
from random import randint

from class_ball import Ball

pygame.init()

sc = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
FPS = 48
x = y = 200
ball1 = Ball(sc, (y, x), (250, 50, 50), 20, (0, 0))
flag = False


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            temp = Ball(sc, event.pos, (0, 0, 0), 10, (randint(-30, 30), randint(-30, 30)))
            flag = True
        elif event.type == pygame.MOUSEWHEEL:
            temp = Ball(sc, (sc.get_size()[0]//2, sc.get_size()[1]//2), 'RANDOM', 10, (randint(-30, 30), randint(-30, 30)))

    sc.fill((100, 100, 220))

    for n, ball in enumerate(ball1.EXAMPLES):
        if flag:
            ball.speed_up(100)
        ball.color_of_speed()
        ball.speed_limit(30)
        for i in range(n + 1, len(ball1.EXAMPLES)):
            ball.clash(ball1.EXAMPLES[i])
        ball._move()
        ball._show()
        ball.speed_slow(.1)
    flag = False

    pygame.display.update()

    clock.tick(FPS)
