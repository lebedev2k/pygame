import pygame

STEP = 10
GRAVITY = 0.2
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
        self.velX = 0

    def update(self, left, right, up, platforms):
        # print(up)
        if left:
            self.velX = -STEP
        if right:
            self.velX = STEP

        if not (left or right):
            self.velX = 0

        if not self.onGround:
            self.velY += GRAVITY

        if up and self.onGround:
            self.velY += -JUMP
            self.onGround = False

        self.rect.x += self.velX
        self.onGround = False
        self.check_collide(platforms, up)

        self.rect.y += self.velY
        self.check_collide(platforms, up)

    def check_collide(self, platforms, up):
        for p in platforms:
            if self.rect.colliderect(p.rect):
                if not up and self.velX > 0:
                    self.rect.right = p.rect.left

                if not up and self.velX < 0:
                    self.rect.left = p.rect.right

                if up and self.velY > 0:
                    self.rect.bottom = p.rect.top
                    self.velY = 0
                    self.onGround = True

                if up and self.velY < 0:
                    self.rect.top = p.rect.bottom
                    self.velY = 0
