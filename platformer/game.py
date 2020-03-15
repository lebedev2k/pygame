import pygame
import sys
from platforma import *
from hero import *

pygame.init()
win = pygame.display.set_mode((640, 320))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()

#bgg = pygame.image.load('img\TileSet_08.png')

bg = pygame.image.load('./img/Background.png')
#bg = pygame.Surface((640, 320))
#bg.fill((100, 100, 100))

pl_group = pygame.sprite.Group()
x = 0
y = 0
for row in level1:
    for col in row:
        if col == '-':
            p = Platform(x, y)
            pl_group.add(p)
        x += PLATFORM_WIDTH
    x = 0
    y += PLATFORM_HEIGHT

hero = Hero(50, 50)
h_group = pygame.sprite.Group()
h_group.add(hero)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    win.blit(bg, (0, 0))
    #win.blit(bgg, (100, 100))
    #win.blit(p.image, (p.rect.x, p.rect.y))
    pl_group.draw(win)
    h_group.draw(win)

    pygame.display.update()
    clock.tick(30)
