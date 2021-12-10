# Advent of code Year 2021 Day 6 solution
# Author = Stijn-Jacobs
# Date = December 2021
from collections import OrderedDict

import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readline()


def process_lantern_fish(inp, day_limit):
    arr = list(map(int, inp.split(",")))

    # Setup initial fishes, and dict that stores amounts of each, with 0 to 8
    dict = OrderedDict(zip([i for i in range(0, 9)], np.zeros(9, int)))
    for fish in arr:
        dict[fish] = dict.get(fish, 0) + 1

    i = 0
    nul_count = 0
    while i <= day_limit:
        # Add new fishes from previous day
        dict[8] = dict.get(8, 0) + nul_count
        nul_count = dict[0]

        temp = dict.copy()
        for val, count in dict.items():
            if val <= 0:
                continue
            temp[val - 1] = temp.get(val, 0)
            temp[val] = 0
        dict = temp

        # Set fishes that duplicated to 6
        dict[6] = dict.get(6, 0) + nul_count

        i += 1
    return sum(dict.values())


print("Part One : " + str(process_lantern_fish(input, 80)))

print("Part Two : " + str(process_lantern_fish(input, 256)))
