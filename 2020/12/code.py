# Advent of code Year 2020 Day 12 solution
# Author = Stijn-Jacobs
# Date = December 2020

import re
import math

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

input = [line.rstrip() for line in input]  # filters out the newline characters

NORTH = (0, 1)
EAST = (1, 0)
SOUTH = (0, -1)
WEST = (-1, 0)

degrees_map = {0: NORTH, 90: EAST, 180: SOUTH, 270: WEST}


def rotate(origin, point, angle):
    angle *= -1
    angle = math.radians(angle)
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy


def get_direction(char, default):
    if char == "N":
        return NORTH
    elif char == "E":
        return EAST
    elif char == "S":
        return SOUTH
    elif char == "W":
        return WEST
    return default


class Ferry:
    def __init__(self, instructions):
        self.instructions = instructions

    def run_with_waypoint(self):
        boat_x, boat_y, orientation = 0, 0, 90
        way_off_x, way_off_y = 10, 1  # relative coordinates

        for instruction in self.instructions:
            split = re.findall("\d+|\D+", instruction)
            char, val = split[0], int(split[1])
            if char == "L" or char == "R":
                # because of the relative coordinates, a lot of calculations
                rotated = rotate((boat_x, boat_y), (way_off_x + boat_x, way_off_y + boat_y),
                                 val if char == "R" else val * -1)
                way_off_x, way_off_y = rotated[0] - boat_x, rotated[1] - boat_y
                continue
            if char == "F":
                boat_x += (way_off_x * val)
                boat_y += (way_off_y * val)
                continue

            dir = get_direction(char, None)

            way_off_x += (dir[0] * val)
            way_off_y += (dir[1] * val)
        return math.floor(abs(boat_x) + abs(boat_y))

    def run_instructions(self):
        x, y, orientation = 0, 0, 90
        for instruction in self.instructions:
            split = re.findall("\d+|\D+", instruction)
            char, val = split[0], int(split[1])
            if char == "L" or char == "R":
                orientation += val if char == "R" else val * -1
                orientation %= 360
                continue

            dir = degrees_map[orientation]
            dir = get_direction(char, dir)

            x += (dir[0] * val)
            y += (dir[1] * val)
        return abs(x) + abs(y)


fer = Ferry(input)
print("Part One : " + str(fer.run_instructions()))

print("Part Two : " + str(fer.run_with_waypoint()))
