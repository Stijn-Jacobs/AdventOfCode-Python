# Advent of code Year 2021 Day 15 solution
# Author = Stijn-Jacobs
# Date = December 2021

import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def get_lowest_risk_path(map):
    grid = Grid(matrix=map)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
    start = grid.node(0, 0)
    end = grid.node(len(map[0]) - 1, len(map) - 1)
    path, runs = finder.find_path(start, end, grid)
    sum = 0
    for node in path[1:]:
        sum += map[node[1]][node[0]]
    return sum


def get_map(inp):
    return np.array([[int(char) for char in line.strip()] for line in inp], int)


# Create the 5x5 map
def get_full_map(inp):
    original = np.array([[int(char) for char in line.strip()] for line in inp], int)
    map = None
    for x in range(0, 5):
        temp = original.copy()
        temp = temp + x
        temp[temp > 9] = temp[temp > 9] - 9

        for y in range(1, 5):
            # Repeat vertical 5 times
            new = original.copy()
            new = new + y + x
            new[new > 9] = new[new > 9] - 9
            temp = np.concatenate((temp, new), axis=0)

        if map is None:
            map = temp.copy()
        else:
            map = np.concatenate((map, temp), axis=1)
    return map


print("Part One :" + str(get_lowest_risk_path(get_map(input))))

print("Part Two :" + str(get_lowest_risk_path(get_full_map(input))))
