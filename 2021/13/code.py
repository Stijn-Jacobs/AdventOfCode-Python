# Advent of code Year 2021 Day 13 solution
# Author = Stijn-Jacobs
# Date = December 2021
from math import ceil

import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def get_map(inp):
    folds = inp[inp.index("\n") + 1:]

    points = inp.copy()
    points.remove("\n")
    for fold in folds:
        points.remove(fold)

    x_arr = [int(split.split(",")[0]) for split in points]
    y_arr = [int(split.split(",")[1].strip()) for split in points]

    # Empty map
    map = np.zeros((max(y_arr) + 1, max(x_arr) + 1), int)
    for (x, y) in zip(x_arr, y_arr):
        map[y][x] = 1
    return map


def execute_fold_from_line(fold, map):
    at = fold.strip().split(" ")[2].split("=")
    if at[0] == "y":
        map = fold_map(map, along_y=int(at[1]))
    else:
        map = fold_map(map, along_x=int(at[1]))
    return map


def fold_map(map, along_y=None, along_x=None):
    if along_y:
        fold_axis = along_y
        top = map[:fold_axis]
        bottom = np.flipud(map[fold_axis + 1:])
        top_largest = len(top) > len(bottom)

        return merge_maps(top if top_largest else bottom, bottom if top_largest else top, bottom=True)
    else:
        fold_axis = along_x
        left = [val[:fold_axis] for val in map]
        right = np.fliplr([val[fold_axis + 1:] for val in map])

        left_largest = len(left[0]) > len(right[0])
        return np.array(merge_maps(left if left_largest else right, right if left_largest else left, right=True))


def merge_maps(map, map_to_merge, bottom=False, right=False):
    diff = 0
    if right:
        diff = len(map[0]) - len(map_to_merge[0])
    elif bottom:
        diff = len(map) - len(map_to_merge)

    for y in range(0, len(map)):
        for x in range(diff, len(map[y])):
            map[y][x] = 1 if map[y][x] >= 1 or (map_to_merge[y - diff][x] >= 1) else 0
    return map


def part1(inp):
    map = get_map(inp)
    fold = inp[inp.index("\n") + 1:][0]
    map = execute_fold_from_line(fold, map)
    return sum(map.flatten())


def part2(inp):
    map = get_map(inp)
    for fold in inp[inp.index("\n") + 1:]:
        map = execute_fold_from_line(fold, map)

    response = "\n"
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):
            char = map[y][x]
            response += "#" if char == 1 else " "
        response += "\n"
    return response


print("Part One : " + str(part1(input)))

print("Part Two : " + str(part2(input)))
