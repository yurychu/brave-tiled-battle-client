from game.engine import Game, Level
from config import window, colors

from levels import StartLevel


def start_game():
    game = Game(window.RESOLUTION, 'Brave Tiled Battle')

    level = StartLevel(game.display_surface, colors.GRAY)
    game.run(window.FPS, level)

if __name__ == '__main__':
    start_game()
