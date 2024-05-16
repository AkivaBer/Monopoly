from Monopoly.gameboard import *


def main():
    board_height = 500
    num_pieces_on_go = 4
    gameboard = Gameboard(board_height)
    gameboard.run()

if __name__ == "__main__":
    main()
