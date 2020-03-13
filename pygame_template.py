import pygame
from sys import exit

pygame.init()
win = pygame.display.set_mode((1050, 500))
pygame.display.set_caption('Pygame template')
clock = pygame.time.Clock()


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.fill((100, 255, 0))

    pygame.display.update()
    clock.tick(30)
