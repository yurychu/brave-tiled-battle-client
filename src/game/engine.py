import sys

import pygame
from pygame.locals import *


class Game(object):

    def __init__(self, resolution, caption):
        pygame.init()
        self.display_surface = pygame.display.set_mode(resolution)
        pygame.display.set_caption(caption)
        self.fps_clock = pygame.time.Clock()

    def run(self, fps, level):
        while True:
            level.draw()

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.fps_clock.tick(fps)


class Level(object):

    def __init__(self, display_surace, bg_color):
        self.display_surface = display_surace
        self.bg_color = bg_color

    def draw(self):
        self.display_surface.fill(self.bg_color)
