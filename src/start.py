from game.engine import Display, Game
from conf import RESOLUTION


def start_game():
    display = Display(RESOLUTION, 'Hello Mean!')
    game = Game(display.displaysurf)
    game.game_loop()


if __name__ == '__main__':
    start_game()
