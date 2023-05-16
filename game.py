import pygame

pygame.init()

pygame.display.set_mode((600, 400), pygame.RESIZABLE)
pygame.display.set_caption("MyGame")
pygame.display.set_icon(pygame.image.load("icon.bmp"))

clock = pygame.time.Clock()
FPS = 60

#running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            # pygame.quit()
            # running = False
        # pygame.time.delay(20)
        clock.tick(FPS)
# print('Done')
