import pygame

STEP = 10
JUMP = 10
GRAVITY = 1


class Hero (pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        a = pygame.image.load('./img/2_enemies_1_walk_000.png')
        self.image = pygame.transform.scale(a, (48, 48))
        #self.image = pygame.Surface((32, 32))
        #self.image.fill((255, 100, 0))

        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
        self.onGround = False
        self.velY = 0

    def update(self, left, right, up, platforms):
        if left:
            self.rect.x -= STEP
        if right:
            self.rect.x += STEP

        if not self.onGround:
            self.velY += GRAVITY

        print(self.onGround)
        if up and self.onGround:
            self.velY -= JUMP

        self.onGround = False
        self.rect.y += self.velY
        self.check_collide(platforms)

    def check_collide(self, platforms):
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if self.velY > 0:
                    self.rect.bottom = p.rect.top
                    self.velY = 0
                    self.onGround = True
                if self.velY < 0:
                    self.rect.top = p.rect.bottom
                    self.velY = 0
