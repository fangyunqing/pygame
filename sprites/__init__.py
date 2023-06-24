import pygame
from settings.settings import *


class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, suf, group, z):
        super(Generic, self).__init__(group)
        self.image = suf
        self.rect = self.image.get_rect(topleft=pos)
        self.z = z


class Water(Generic):
    def __init__(self, pos, frames, group):
        self.frames = frames
        self.frame_index = 0

        super().__init__(pos, self.frames[self.frame_index], group, LAYERS["main"])

    def animate(self, dt):
        self.frame_index += 5 * dt
        if self.frame_index > len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, dt):
        self.animate(dt)


class WildFlower(Generic):
    def __init__(self, pos, suf, group):
        super().__init__(pos, suf, group, LAYERS["main"])


class Tree(Generic):
    def __init__(self, pos, suf, group, name):
        super().__init__(pos, suf, group, LAYERS["main"])