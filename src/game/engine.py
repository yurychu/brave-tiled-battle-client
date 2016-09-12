import sys

import pygame
from pygame.locals import *


class Display(object):

    def __init__(self, resolution, text_caption):
        pygame.init()
        self.displaysurf = pygame.display.set_mode(resolution)
        pygame.display.set_caption(text_caption)


class Game(object):

    def __init__(self, displaysurf, level):
        self.displaysurf = displaysurf
        self.level = level

    def system_events(self):
        pass

    def game_loop(self):
        while True:
            self.level.init_state()
            self.level.events_handling()
            self.level.do_actions()
            self.level.update()


class Level(object):

    def __init__(self, level_objects):
        self.level_objects = level_objects

    def init_state(self):
        for level_object in self.level_objects:
            level_object.set_state()

    def events_handling(self):
        for level_object in self.level_objects:
            level_object.events()

    def do_actions(self):
        for level_object in self.level_objects:
            level_object.actions()

    def update(self):
        pygame.display.update()
