import sys

from crack_the_code import CrackTheCodeGame


def play_again():
    res = input("Do you want to play again ? (y/n)").strip().lower()[0:1]
    play_game() if res == 'y' else sys.exit()


def play_game():
    game = CrackTheCodeGame()
    game.play()
    play_again()


def main():
    play_game()


if __name__ == "__main__":
    main()