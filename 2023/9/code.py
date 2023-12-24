# Advent of code Year 2023 Day 9 solution
# Author = Stijn-Jacobs
# Date = December 2023
import math

import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


class Row:
    def __init__(self, row):
        self.row = row


def calc_rows(inp):
    # split on space and convert to int
    line = [int(x) for x in inp.split()]
    rows = [line]
    diff_list = line
    while True:
        # create list of the differences between the numbers next to each other
        diff_list = [diff_list[i + 1] - diff_list[i] for i in range(len(diff_list) - 1)]

        if all(dif == 0 for dif in diff_list):
            break
        else:
            rows.append(diff_list)

    rows.reverse()
    return rows


def extrapolate(left):
    sum = 0
    for line in input:
        rows = calc_rows(line)

        # add values so we can extrapolate
        rows[0].append(rows[0][0])

        if left:
            # extrapolate, the value on the left
            for i in range(len(rows[1:])):
                # add new value using the previous value, and the value from the row above
                rows[i + 1].insert(0, rows[i + 1][0] - rows[i + 1 - 1][0])

            sum += rows[-1][0]
        else:
            # extrapolate, by 1 value each time for each row
            for i in range(len(rows[1:])):
                # add new value using the previous value, and the value from the row above
                rows[i + 1].append(rows[i + 1 - 1][-1] + rows[i + 1][-1])

            sum += rows[-1][-1]

    return sum


def part1():
    return extrapolate(False)


def part2():
    return extrapolate(True)


print(part1())
print(part2())
