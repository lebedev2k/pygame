# 2020-03-26 Добавлена анимация при перемещении героя.

import pygame
import pyganim

STEP = 2
GRAVITY = 0.2
JUMP = 7
DELAY = 100
FILL_COLOR = (170, 0, 0)

imgRight = [
    ('platformer/img/2_enemies_1_walk_000.png', DELAY),
    ('platformer/img/2_enemies_1_walk_001.png', DELAY),
    ('platformer/img/2_enemies_1_walk_002.png', DELAY),
    ('platformer/img/2_enemies_1_walk_003.png', DELAY),
    ('platformer/img/2_enemies_1_walk_004.png', DELAY),
    ('platformer/img/2_enemies_1_walk_005.png', DELAY)
]

imgStand = pygame.image.load('platformer/img/2_enemies_1_walk_000.png')
imgStand = pygame.transform.scale(imgStand, (32, 32))


heroAnimRight = pyganim.PygAnimation(imgRight)
heroAnimRight.scale((32, 32))
heroAnimRight.play()

heroAnimLeft = heroAnimRight.getCopy()
heroAnimLeft.flip(True, False)
heroAnimLeft.play()


class Hero (pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        # a = pygame.image.load('./img/2_enemies_1_walk_000.png')
        # self.image = pygame.transform.scale(a, (48, 48))
        self.image = pygame.Surface((32, 32))
        self.image.fill(FILL_COLOR)
        self.image.set_colorkey(FILL_COLOR)

        self.rect = self.image.get_rect()
        # self.rect = pygame.Rect(0, 0, 20, 32)  # self.image.get_rect()
        self.rect.move_ip(x, y)
        self.onGround = False
        self.velY = 0
        self.velX = 0

    def update(self, left, right, up, platforms):
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
        self.check_collide(platforms, False)

        self.onGround = False
        self.rect.y += self.velY
        self.check_collide(platforms, True)

        self.image.fill(FILL_COLOR)
        if right:
            heroAnimRight.blit(self.image, (0, 0))
        if left:
            heroAnimLeft.blit(self.image, (0, 0))
        if not left and not right:
            self.image.blit(imgStand, (0, 0))

    def check_collide(self, platforms, up):
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

    # def draw(self):
    #     print('draw')
    #     heroAnim.blit(self.image, (0, 0))
