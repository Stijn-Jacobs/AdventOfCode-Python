# Advent of code Year 2021 Day 4 solution
# Author = Stijn-Jacobs
# Date = December 2021

import re
import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


class Board:
    def __init__(self, board):
        self.board = board

    def has_won(self, winning_numbers):
        # horizontal
        for row in self.board:
            if all(item in winning_numbers for item in row):
                return True

        # vertical
        for column in zip(*self.board):
            if all(item in winning_numbers for item in column):
                return True

    def get_unmarked(self, winning_numbers):
        flat = np.array(self.board).flatten()
        unique_numbers = np.unique(flat, axis=0)
        indices = np.argwhere(np.isin(unique_numbers, winning_numbers))
        unique_numbers = np.delete(unique_numbers, indices)
        return list(map(int, unique_numbers))


complete_winning_numbers = input[0].strip().split(",")

# Remove first 2 rows
input = input[2:]
boards = []

# Convert text to board models
arr = []
for line in input:
    if line == '\n':
        boards.append(Board(arr.copy()))
        arr.clear()
        continue
    arr.append(re.split("  | ", line.strip()))


def find_winning_board(boards, winning_numbers, reversed):
    iteration = 1
    while True:
        cur_winning_numbers = winning_numbers[:iteration]
        iteration += 1
        temp_boards = boards.copy()
        for board in boards:
            if board.has_won(cur_winning_numbers):
                if reversed and len(temp_boards) == 1:
                    unmarked_sum = sum(boards[0].get_unmarked(cur_winning_numbers))
                    return unmarked_sum * int(cur_winning_numbers[-1])
                elif not reversed:
                    unmarked_sum = sum(board.get_unmarked(cur_winning_numbers))
                    return unmarked_sum * int(cur_winning_numbers[-1])
                temp_boards.remove(board)
        boards = temp_boards


print("Part One : " + str(find_winning_board(boards, complete_winning_numbers, False)))

print("Part Two : " + str(find_winning_board(boards, complete_winning_numbers, True)))
