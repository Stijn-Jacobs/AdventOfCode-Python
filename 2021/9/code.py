# Advent of code Year 2021 Day 9 solution
# Author = Stijn-Jacobs
# Date = December 2021

import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

map = np.array([[int(char) for char in line.strip()] for line in input], int)


# Checks if given point is lower than all adjacent (not diagonal) points
def lower_then_surrounding(x, y):
    origin_val = map[y][x]
    if y >= 0 and map[y - 1][x] <= origin_val:
        return False
    elif len(map) - 1 > y and map[y + 1][x] <= origin_val:
        return False
    elif x >= 0 and map[y][x - 1] <= origin_val:
        return False
    elif len(map[y]) - 1 > x and map[y][x + 1] <= origin_val:
        return False
    return True


def get_lowest_points():
    points = []
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            if lower_then_surrounding(x, y):
                points.append((x, y))
    return points


def calculate_risk_score():
    risk = 0
    for point in get_lowest_points():
        risk += map[point[1]][point[0]] + 1
    return risk


# Returns basin size from from current position
def spread(x, y, explored_map):
    # Check if already checked, and if in bounds
    if explored_map.get((x, y), False):
        return 0
    spread_sum = 0
    explored_map[(x, y)] = True

    if x + 1 < len(map[y]) and map[y][x + 1] != 9:
        spread_sum += spread(x + 1, y, explored_map)
    if x > 0 and map[y][x - 1] != 9:
        spread_sum += spread(x - 1, y, explored_map)
    if y + 1 < len(map) and map[y + 1][x] != 9:
        spread_sum += spread(x, y + 1, explored_map)
    if y > 0 and map[y - 1][x] != 9:
        spread_sum += spread(x, y - 1, explored_map)

    return spread_sum + 1


def find_largests_basins():
    basin_sizes = []
    for point in get_lowest_points():
        size = spread(point[0], point[1], {})
        basin_sizes.append(size)
    basin_sizes.sort(reverse=True)
    # Mul 3 largest
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


print("Part One : " + str(calculate_risk_score()))

print("Part Two : " + str(find_largests_basins()))
