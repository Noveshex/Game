from random import randint
import pygame
from balls import Ball

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 2000)

WIDTH, HEIGHT = 600, 400

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

balls_data = (
    {'path': 'ball_1.png', 'score': 100},
    {'path': 'ball_2.png', 'score': 200}
)

pygame.mixer.music.load('sounds/football_sound.mp3')
sound_catch = pygame.mixer.Sound('sounds/catch.ogg')
pygame.mixer.music.play(-1)
window = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("MyGame")
pygame.display.set_icon(pygame.image.load("img/icon.bmp"))
clock = pygame.time.Clock()
FPS = 60
score = pygame.image.load('img/score_fon.png').convert_alpha()
font = pygame.font.SysFont('arial', 30)
balls_surf = [pygame.image.load('img/' + data['path']).convert_alpha() for data in balls_data]
telega = pygame.image.load('img/telega.png').convert_alpha()
t_rect = telega.get_rect(centerx=WIDTH//2, bottom=HEIGHT-5)
background = pygame.image.load('img/football.jpg').convert()
balls = pygame.sprite.Group()

volume_icon = pygame.image.load('img/volume.png').convert_alpha()
volume_icon = pygame.transform.scale(volume_icon, (30, 30))
volume_rect = volume_icon.get_rect(topright=(WIDTH-10, 10))


def createBall(group):
    indx = randint(0, len(balls_surf)-1)
    x = randint(20, WIDTH-20)
    speed = randint(1,4)

    return Ball(x, speed, balls_surf[indx], balls_data[indx]['score'], group)


game_score = 0

def collideBalls():
    global game_score
    for ball in balls:
        if t_rect.collidepoint(ball.rect.center):
            sound_catch.play()
            game_score += ball.score
            ball.kill()

musicPause = False
vol = 1.0
speed = 10
createBall(balls)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.USEREVENT:
            createBall(balls)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                musicPause = not musicPause
                if musicPause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_DOWN:
                vol -= 0.1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_UP:
                vol += 0.1
                pygame.mixer.music.set_volume(vol)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        t_rect.x -= speed
        if t_rect.x < 0:
            t_rect.x = 0
    elif keys[pygame.K_RIGHT]:
        t_rect.x += speed
        if t_rect.x > WIDTH - t_rect.width:
            t_rect.x = WIDTH - t_rect.width

    collideBalls()
    window.blit(background, (0, 0))
    window.blit(score, (5, 5))
    window.blit(volume_icon, volume_rect)
    vol_percent = int(vol * 100)
    vol_text = font.render(f"Volume: {vol_percent}%", 1, (0, 0, 0))
    window.blit(vol_text, (380, 8))
    window_text = font.render(str(game_score), 1, (94, 138, 14))
    window.blit(window_text, (20, 10))
    balls.draw(window)
    window.blit(telega, t_rect)
    pygame.display.update()

    clock.tick(FPS)

    balls.update(HEIGHT)






