import pygame
from platforma import PLATFORM_WIDTH, PLATFORM_HEIGHT
from utils import *
import pyganim


class Bonus (pygame.sprite.Sprite):

    def __init__(self, x, y, dirname):
        super().__init__()
        self.bgcolor = (255, 100, 0)
        self.image = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(self.bgcolor)
        self.image.set_colorkey(self.bgcolor)

        self.rect = self.image.get_rect()
        self.rect.move_ip(x, y)

        self.animImages = getPygAnimListFromDir(dirname, 200)
        # создаем объект анимации
        self.anim = pyganim.PygAnimation(self.animImages)
        self.anim.scale((32, 32))
        self.anim.play()

    def update(self):
        self.image.fill(self.bgcolor)
        self.anim.blit(self.image, (0, 0))
