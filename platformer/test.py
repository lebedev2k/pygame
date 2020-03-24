import pygame
import pyganim

pygame.init()

# a = [
#     ('.\walk001.png', 100),

# ]
# anim = pyganim.PygAnimation(a)
# anim.play()

win = pygame.display.set_mode((640, 320))
pygame.display.set_caption('Platformer')
clock = pygame.time.Clock()

bk = pygame.image.load('platformer/img/2_enemies_1_walk_000.png')
s = pygame.Surface((300, 300))
s.blit(bk, (0, 0))

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
    win.blit(bk, (0, 0))
    pygame.display.update()
    clock.tick(30)
