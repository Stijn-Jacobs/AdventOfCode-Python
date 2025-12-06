# Advent of code Year 2025 Day 6 solution
# Author = Stijn-Jacobs
# Date = December 2025
import math
import re

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

map = []

only_spaces = set()

# find the indexes with only spaces on each line first
for x in range(len(input[0])):
    only_spaces.add(x)
    for l in input:
        if x >= len(l):
            continue
        c = l[x]
        if x in only_spaces and c != ' ':
            only_spaces.remove(x)

# now split all lines on those indexes
for l in input:
    row = []
    last_index = 0
    for index in sorted(only_spaces):
        if index > len(l):
            continue
        row.append(l[last_index:index])
        last_index = index + 1
    row.append(l[last_index:].strip())
    map.append(row)

def part_1():
    total = 0
    for r in range(len(map[0])):
        vals = []
        for col in range(len(map)):
            c = map[col][r].strip()
            if c == '*':
                total += math.prod(vals)
            elif c == '+':
                total += sum(vals)
            else:
                vals.append(int(c))

    return total

def part_2():
    total = 0
    for col in range(len(map[0])):
        nums = []
        for length in range(max(len(r[col]) for r in map)):
            cur_num = ""
            for number_row in range(len(map) - 1):
                index_in_row = len(map[0][col]) - length - 1
                if index_in_row > len(map[number_row][col]) - 1:
                    continue

                cur_num += map[number_row][col][index_in_row].strip()

            if cur_num != "":
                nums.append(int(cur_num))

        # get the correct operator from the first index of the last row.
        if map[len(map) - 1][col][0] == "*":
            total += math.prod(nums)
        elif map[len(map) - 1][col][0] == "+":
            total += sum(nums)

    return total

print(part_1())
print(part_2())