import pygame


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, suf, group, z):
        super(Generic, self).__init__(group)
        self.image = suf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z
