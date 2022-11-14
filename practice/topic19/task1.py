import pygame

pygame.init()

W = 1000
H = 500

sc = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("task1-5")

clock = pygame.time.Clock()
FPS = 30

R, G, B = 50, 250, 50
BACKGROUND = (250,250,200)


whith_ball = 60
height_ball = 60

x = W // 2
y = H // 2
speed = 5
friction_force = .9


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    keys = pygame.key.get_pressed()

    if x < 1:
        speed += 1
        speed *= -1
        x = 1
    elif x > W - whith_ball:
        speed -= 1
        speed *= -1
        x = W - whith_ball - 1



    if keys[pygame.K_LEFT]:
        speed -= 1

    elif keys[pygame.K_RIGHT]:
        speed += 1

    speed -= 0.0098 * speed

    x += int(speed)
    if abs(speed) > 58:
        speed = 58

    sc.fill(BACKGROUND)
    ball = pygame.draw.ellipse(sc,(int(R + abs(speed) * 3.5), int(G - abs(speed) * 3.5), B),(x, y, whith_ball, height_ball) )
    pygame.display.update()

    clock.tick(FPS)
