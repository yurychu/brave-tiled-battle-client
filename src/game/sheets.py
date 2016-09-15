import pygame

import config


class TileSheet(object):

    def __init__(self, file_name):
        self.tile_sheet = pygame.image.load(file_name).convert()

    def get_image(self, x, y, width, height):
        image = pygame.Surface([width, height]).convert()
        image.blit(
            self.tile_sheet,
            (0, 0),
            (x, y, width, height)
        )
        image.set_colorkey(config.BLACK)
        return image
