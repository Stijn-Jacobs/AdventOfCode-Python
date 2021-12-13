# Advent of code Year 2021 Day 11 solution
# Author = Stijn-Jacobs
# Date = December 2021

import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def increase_energy(map, x, y, flashed_map, increased_map, forced=False):
    if flashed_map.get((x, y), False):
        return 0
    # Check bounds
    if 0 <= y < len(map) and 0 <= x < len(map[y]):
        if map[y][x] >= 9:
            flashes = 0
            flashed_map[(x, y)] = True
            # Flash surroundings
            for xmod in range(-1, 2):
                for ymod in range(-1, 2):
                    newx = x + xmod
                    newy = y + ymod
                    flashes += increase_energy(map, newx, newy, flashed_map, increased_map, True)
            return flashes + 1
        elif forced or not increased_map.get((x, y), False):
            map[y][x] = map[y][x] + 1
            if not forced:
                increased_map[(x, y)] = True
    return 0


def simulate_steps_flash_sum(inp, steps=None, find_synchronised_step=False):
    map = np.array([[int(char) for char in line.strip()] for line in input], int)

    flash_sum = 0
    i = 0
    while find_synchronised_step or i < steps:
        i += 1
        flashed_map = {}
        increased_map = {}
        for y in range(0, len(inp)):
            for x in range(0, len(inp[y])):
                flash_sum += increase_energy(map, x, y, flashed_map, increased_map)
        for item in flashed_map.keys():
            map[item[1]][item[0]] = 0
        if find_synchronised_step and len(flashed_map) == len(map.flatten()):
            # Synchronised
            return i
    return flash_sum


print("Part One : " + str(simulate_steps_flash_sum(input, steps=100)))

print("Part Two : " + str(simulate_steps_flash_sum(input, find_synchronised_step=True)))
