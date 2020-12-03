# Advent of code Year 2020 Day 3 solution
# Author = Stijn-Jacobs
# Date = December 2020

import math

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

mapWidth = len(input[0].rstrip())
mapHeight = len(input)

map = [[0 for x in range(mapWidth)] for y in range(mapHeight)]

# fill map
for lineIndex, line in enumerate(input):
    for charIndex, char in enumerate(input[lineIndex].rstrip()):
        map[lineIndex][charIndex] = char


def check_map_with_slope(x_slope, y_slope, map):
    x = 0
    y = 0

    trees = 0

    while y < len(map):
        if map[y][x] == "#":
            trees += 1
        x += x_slope
        y += y_slope
        if x >= mapWidth:
            x -= mapWidth

    return trees


print("Part One : " + str(check_map_with_slope(x_slope=3, y_slope=1, map=map)))

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
results = []
for slope in slopes:
    results.append(check_map_with_slope(slope[0], slope[1], map=map))

print("Part Two : " + str(math.prod(results)))
