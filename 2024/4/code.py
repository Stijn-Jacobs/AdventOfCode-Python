# Advent of code Year 2024 Day 4 solution
# Author = Stijn-Jacobs
# Date = December 2024
import re

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

word = list("XMAS")

def parse_input(input):
    return [list(line.strip()) for line in input]

def check_adjacent(map, x, y, offset_x, offset_y, expected):
    # check bounds
    if x + offset_x < 0 or x + offset_x >= len(map) or y + offset_y < 0 or y + offset_y >= len(map[x]):
        return False
    return map[x + offset_x][y + offset_y] == expected

def solve1(input):
    # create 2 array of the input
    map = parse_input(input)
    sum = 0

    for x in range(0, len(map)):
        for y in range(0, len(map[x])):
            # check all 8 directions
            if map[x][y] != word[0]:
                continue

            for off_x in range(-1, 2):
                for off_y in range(-1, 2):
                    # check bounds, and skip the current position
                    if off_x == 0 and off_y == 0:
                        continue
                    for delta in range(0, len(word)):
                        if check_adjacent(map, x, y, off_x * delta, off_y * delta, word[delta]):
                            if delta == len(word) - 1:
                                sum += 1
                        else:
                            break
    return sum

def solve2(input):
    map = parse_input(input)
    sum = 0

    for x in range(0, len(map)):
        for y in range(0, len(map[x])):
            if map[x][y] != 'A':
                continue

            found = True
            for off_x in range(-1, 2):
                for off_y in range(-1, 2):
                    if off_x == 0 or off_y == 0:
                        continue

                    if not (check_adjacent(map, x, y, off_x, off_y, 'M')
                        or check_adjacent(map, x, y, off_x, off_y, 'S')):
                        found = False
                        break
                    else:
                        # if we find an M or S, we need to check if the other is present
                        if check_adjacent(map, x, y, off_x, off_y, 'M'):
                            if not check_adjacent(map, x, y, -off_x, -off_y, 'S'):
                                found = False
                                break
                        else:
                            if not check_adjacent(map, x, y, -off_x, -off_y, 'M'):
                                found = False
                                break
                if not found:
                    break

            if found:
                sum += 1


    return sum

print(solve1(input))
print(solve2(input))