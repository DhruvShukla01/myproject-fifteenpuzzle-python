# author: Dhruv Shukla
# date: May 29, 2023
# file: fifteen.py a Python program that implements class Fifteen with various function for Fifteen Puzzle game
# input: No input from the user taken directly
# output: interactive text messages and a fifteen puzzle game.

import numpy as np
from random import choice


class Fifteen:

    def __init__(self, size=4):
        self.tiles = np.array([i for i in range(1, size ** 2)] + [0])
        self.adjacent = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 7], [0, 5, 8], [1, 4, 6, 9], [2, 5, 7,10], [3, 6, 8, 11],
                         [4, 7, 9, 12], [5, 8, 10, 13], [6, 9, 11, 14], [7, 10, 15], [8, 13], [9, 12, 14], [10, 13, 15],
                         [11, 14]]
    def update(self, move):
        if self.is_valid_move(move):
            ind = np.where(self.tiles == move)[0][0]
            for i in self.adjacent[ind]:
                if self.tiles[i] == 0:
                    self.transpose(ind, i)

    def transpose(self, i, j):
        self.tiles[i], self.tiles[j] = self.tiles[j], self.tiles[i]

    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)
        index = index[0][0]
        for i in range(steps):
            move_index = choice(self.adjacent[index])
            self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index]
            index = move_index

    def is_valid_move(self, move):
        ind = np.where(self.tiles == move)
        ind = ind[0][0]
        for i in self.adjacent[ind]:
            if self.tiles[i] == 0:
                return True
        return False

    def is_solved(self):
        return np.array_equal(self.tiles[:-1], np.arange(1, len(self.tiles)))

    def draw(self):
        print(f"+---+---+---+---+\n"
              f"| {self.tiles[0]} | {self.tiles[1]} | {self.tiles[2]} | {self.tiles[3]} |\n"
              f"+---+---+---+---+\n"
              f"| {self.tiles[4]} | {self.tiles[5]} | {self.tiles[6]} | {self.tiles[7]} |\n"
              f"+---+---+---+---+\n"
              f"| {self.tiles[8]} | {self.tiles[9]} | {self.tiles[10]} | {self.tiles[11]} |\n"
              f"+---+---+---+---+\n"
              f"| {self.tiles[12]} | {self.tiles[13]} | {self.tiles[14]} |{self.tiles[15]} |\n"
              f"+---+---+---+---+\n")

    def __str__(self):
        size = int(np.sqrt(len(self.tiles)))
        str1 = ""
        for i in range(size):
            for j in range(size):
                tile = self.tiles[i * size + j]
                if tile == 0:
                    str1 += "   "
                else:
                    str1 += f"{tile:2d}" + " "
            str1 += "\n"
        return str1


if __name__ == '__main__':

    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False

    '''You should be able to play the game if you uncomment the code below'''

    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game over!')
