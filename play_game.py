from zombie_invasion.game import Game


def play_game(game=Game()):
    game.set_up()
    game.initial_display()
    game.play()


if __name__ == "__main__":
    play_game()
