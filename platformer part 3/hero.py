import pygame
import pyganim

STEP = 10
GRAVITY = 0.4
JUMP = 10


class Hero (pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        #a = pygame.image.load('./img/2_enemies_1_walk_000.png')
        #self.image = pygame.transform.scale(a, (48, 48))
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 100, 0))

        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.onGround = False
        self.velY = 0

    def update(self, left, right, up, platforms, *plat2):
        if left:
            self.rect.x -= STEP
        if right:
            self.rect.x += STEP

        if not self.onGround:
            self.velY += GRAVITY
        elif up:
            self.velY += -JUMP

        self.onGround = False
        self.check_collide2(platforms, left, right, False, plat2)

        self.rect.y += self.velY
        self.check_collide2(platforms, False, False, True, plat2)

    def check_collide(self, platforms, left, right, up):
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if left:
                    self.rect.left = p.rect.right
                if right:
                    self.rect.right = p.rect.left

                if up and self.velY > 0:
                    self.rect.bottom = p.rect.top
                    self.velY = 0
                    self.onGround = True

                if up and self.velY < 0:
                    self.rect.top = p.rect.bottom
                    self.velY = 0

    def check_collide2(self, platforms, left, right, up, *plat2):
        a = pygame.sprite.spritecollide(self, platforms, False)
        if a:
            if left:
                self.rect.left = a[0].rect.right
            if right:
                self.rect.right = a[0].rect.left

            if up and self.velY > 0:
                self.rect.bottom = a[0].rect.top
                self.velY = 0
                self.onGround = True

            if up and self.velY < 0:
                self.rect.top = a[0].rect.bottom
                self.velY = 0
