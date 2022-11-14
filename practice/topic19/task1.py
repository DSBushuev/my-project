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


whith_circle = 50
height_circle = 50

x = W // 2
y = H // 2
speed = 5


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if x == 0 or x == 500 - whith_circle:
        speed *= -1

    x += speed

    sc.fill(BACKGROUND)
    ball = pygame.draw.ellipse(sc, COLOR,(x, y, whith_circle, height_circle) )
    pygame.display.update()

    clock.tick(FPS)
