import pygame
import pyganim
import os
from utils import getPygAnimListFromDir

STEP = 2
GRAVITY = 0.2
JUMP = 7
DELAY = 100
FILL_COLOR = (170, 0, 0)

path = os.path.dirname(__file__)+'/img/hero'
imgRight = getPygAnimListFromDir(path, 100)

# imgRight = [
#     ('platformer/img/2_enemies_1_walk_000.png', 100),
#     ('platformer/img/2_enemies_1_walk_001.png', 100),
#     ('platformer/img/2_enemies_1_walk_002.png', 100),
#     ('platformer/img/2_enemies_1_walk_003.png', 100),
#     ('platformer/img/2_enemies_1_walk_004.png', 100),
#     ('platformer/img/2_enemies_1_walk_005.png', 100),
#     ('platformer/img/2_enemies_1_walk_006.png', 100),
#     ('platformer/img/2_enemies_1_walk_007.png', 100),
#     ('platformer/img/2_enemies_1_walk_008.png', 100),
# ]

imgStand = pygame.image.load('platformer/img/hero/2_enemies_1_walk_000.png')
imgStand = pygame.transform.scale(imgStand, (32, 32))

animRight = pyganim.PygAnimation(imgRight)
animRight.scale((32, 32))
animRight.play()

animLeft = animRight.getCopy()
animLeft.flip(True, False)
animLeft.play()


class Hero (pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill(FILL_COLOR)
        self.image.set_colorkey(FILL_COLOR)

        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.onGround = False
        self.velY = 0
        self.velX = 0

    def update(self, left, right, up, platforms, platformsX):
        # print(up)
        if left:
            self.velX = -STEP

        if right:
            self.velX = STEP

        if not self.onGround:
            self.velY += GRAVITY

        if up and self.onGround:
            self.velY += -JUMP

        if not left and not right:
            self.velX = 0

        self.rect.x += self.velX
        self.check_collide(platforms, False, platformsX)

        self.onGround = False
        self.rect.y += self.velY
        self.check_collide(platforms, True, platformsX)

        self.image.fill(FILL_COLOR)
        if right:
            #animRight.blit(self.image, (0, 0))
            self.image.blit(imgStand, (0, 0))
        if left:
            #animLeft.blit(self.image, (0, 0))
            self.image.blit(imgStand, (0, 0))

        if not right and not left:
            self.image.blit(imgStand, (0, 0))

    def check_collide(self, platforms, up, platformsX):
        for p in platformsX:
            if self.rect.colliderect(p.rect):
                self.teleport(0, 0)
                return

        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.velY > 0 and up:
                    self.rect.bottom = p.rect.top
                    self.onGround = True
                    self.velY = 0

                if self.velY < 0 and up:
                    self.rect.top = p.rect.bottom
                    self.velY = 0

                if self.velX > 0 and not up:
                    self.rect.right = p.rect.left
                    self.velX = 0

                if self.velX < 0 and not up:
                    self.rect.left = p.rect.right
                    self.velX = 0

    def teleport(self, goX, goY):
        self.rect.x = goX
        self.rect.y = goY
        self.onGround = False
        self.velY = 0
        self.velX = 0

    # def draw(self):
    #     print('draw')
    #     heroAnim.blit(self.image, (0, 0))
