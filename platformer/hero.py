import pygame


class Hero (pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        a = pygame.image.load('./img/2_enemies_1_walk_000.png')
        self.image = pygame.transform.scale(a, (48, 48))
        #self.image = pygame.Surface((32, 32))
        #self.image.fill((255, 100, 0))

        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
