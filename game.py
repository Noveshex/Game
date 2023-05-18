from random import randint
import pygame
from balls import Ball

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

WIDTH, HEIGHT = 600, 400

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("MyGame")
pygame.display.set_icon(pygame.image.load("img/icon.bmp"))
clock = pygame.time.Clock()
FPS = 60

balls_images = ['ball_1.png', 'ball_2.png']
balls_surf = [pygame.image.load('img/' + img).convert_alpha() for img in balls_images]

def createBall(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, WIDTH-20)
    speed = randint(1,4)

    return Ball(x, speed, balls_surf[indx], group)

background = pygame.image.load('img/football.jpg').convert()
balls = pygame.sprite.Group()

speed = 1

createBall(balls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)

    window.blit(background, (0, 0))
    balls.draw(window)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(HEIGHT)






