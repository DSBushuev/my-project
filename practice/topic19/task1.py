import pygame

pygame.init()

W = 500
H = 500

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("task1-5")

clock = pygame.time.Clock()
FPS = 30

R, G, B = 50, 50, 50
COLOR = R,G,B
BACKGROUND = (250,250,200)


whith_ball = 50
height_ball = 50

x = W // 2
y = H // 2
speed = 5


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if x < 1 or x > 499 - whith_ball:
        speed *= -1

    if keys[pygame.K_LEFT]:
        speed -= 1

    elif keys[pygame.K_RIGHT]:
        speed += 1


    x += speed // 2

    sc.fill(BACKGROUND)
    ball = pygame.draw.ellipse(sc, COLOR,(x, y, whith_ball, height_ball) )
    pygame.display.update()

    clock.tick(FPS)
