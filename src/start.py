from game.engine import Game, Level
from config import window, colors


def start_game():
    game = Game(window.RESOLUTION, 'Brave Tiled Battle')

    level = Level(game.display_surface, colors.GRAY)
    game.run(window.FPS, level)

if __name__ == '__main__':
    start_game()
