import pygame

from game.sheets import TileSheet
from game.engine import Level


class TileSet(object):

    def __init__(self, src):
        self.src = TileSheet(src)

    def compile_tileset(self, tile_size):
        tileset = []
        GRASS = self.src.get_image(tile_size * 0, 0, tile_size, tile_size)
        DIRT = self.src.get_image(tile_size * 1, 0, tile_size, tile_size)
        WOOD_BOT = self.src.get_image(tile_size * 2, 0, tile_size, tile_size)
        WOOD_TOP = self.src.get_image(tile_size * 3, 0, tile_size, tile_size)
        SHRUB = self.src.get_image(tile_size * 4, 0, tile_size, tile_size)
        tileset.append(GRASS)
        tileset.append(DIRT)
        tileset.append(WOOD_BOT)
        tileset.append(WOOD_TOP)
        tileset.append(SHRUB)
        return tileset


class StartLevel(Level):

    def draw(self):
        super().draw()
        TILE_SIZE = 64

        GRASS___ = 0
        DIRT____ = 1
        WOOD_BOT = 2
        WOOD_TOP = 3
        SHRUB___ = 4

        tile_map = [
            [WOOD_BOT, WOOD_BOT, DIRT____, GRASS___],
            [GRASS___, DIRT____, DIRT____, SHRUB___],
            [WOOD_TOP, WOOD_TOP, GRASS___, GRASS___],
            [WOOD_BOT, WOOD_BOT, DIRT____, GRASS___]
        ]
        tile_src = TileSet('src/resources/png/map.png')
        tile_set = tile_src.compile_tileset(TILE_SIZE)

        for row in tile_map:
            for tile in row:
                self.display_surface.blit(tile_set[tile], (0, 0))



