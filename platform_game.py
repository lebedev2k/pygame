import pygame
import sys
from platform import *

pygame.init()
win = pygame.display.set_mode((1050, 500))
pygame.display.set_caption('Pygame template')
clock = pygame.time.Clock()

bg = pygame.image.load('img\TileSet_08.png')

pl = Platform()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.blit(bg, (0, 0))

    pygame.display.update()
    clock.tick(30)
