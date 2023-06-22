import pygame

from overlay.overlay import Overlay
from player.player import Player
from sprites import Generic
from settings.settings import *
from pytmx.util_pygame import load_pygame


class Level:
    def __init__(self):
        # get the display surface
        self.display_surface = pygame.display.get_surface()

        # sprite groups
        self.all_sprites = CameraGroup()

        tmx_data = load_pygame(r"/Users/fyq/PycharmProjects/pygame/data/map.tmx")

        # house
        for layer in ["HouseFloor", "HouseFurnitureBottom"]:
            for x, y, suf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), suf, self.all_sprites, LAYERS["house bottom"])

        for layer in ["HouseWalls", "HouseFurnitureTop"]:
            for x, y, suf in tmx_data.get_layer_by_name(layer).tiles():
                Generic((x * TILE_SIZE, y * TILE_SIZE), suf, self.all_sprites, LAYERS["main"])

        for x, y, suf in tmx_data.get_layer_by_name("Fence").tiles():
            Generic((x * TILE_SIZE, y * TILE_SIZE), suf, self.all_sprites, LAYERS["main"])


        Generic(pos=(0, 0),
                suf=(pygame.image.load(r"/Users/fyq/PycharmProjects/pygame/graphics/world/ground.png")
                     .convert_alpha()),
                group=self.all_sprites,
                z=LAYERS["ground"])

        self.player = Player((640, 360), self.all_sprites)

        self.overlay = Overlay(self.player)

    def run(self, dt):
        self.display_surface.fill('black')
        # self.all_sprites.draw(self.display_surface)
        self.all_sprites.customize_draw(self.player)
        self.all_sprites.update(dt)
        self.overlay.display()


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super(CameraGroup, self).__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def customize_draw(self, player):
        self.offset.x = player.rect.centerx - SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - SCREEN_HEIGHT / 2
        for layer in LAYERS.values():
            for sprite in self.sprites():
                if layer == sprite.z:
                    offset_rect = sprite.rect.copy()
                    offset_rect.center -= self.offset
                    self.display_surface.blit(sprite.image, offset_rect)
