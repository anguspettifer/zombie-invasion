from zombie_invasion.game import Game


def play_game(game=Game()):
    game.set_up()
    game.initial_display()
    game.start()


if __name__ == "__main__":
    play_game()
