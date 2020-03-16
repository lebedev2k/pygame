import pygame

level1 = [
    '                    ',
    '                    ',
    '                    ',
    '              ---   ',
    '        ---         ',
    '                    ',
    ' ----               ',
    '         ---        ',
    '                    ',
    '--------------------',
]

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32


class Platform (pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        #self.image = pygame.image.load('img\TileSet_08.png')
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill((0, 100, 0))

        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)
