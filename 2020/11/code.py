# Advent of code Year 2020 Day 11 solution
# Author = Stijn-Jacobs
# Date = December 2020

import copy
import time

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

input = [list(line.rstrip()) for line in input]  # strip new lines


class Area:
    def __init__(self, content):
        self.content = content

    def run(self, rules):
        while True:
            new_content = copy.deepcopy(self.content)
            for x in range(0, len(self.content)):
                for y in range(0, len(self.content[0])):
                    if rules == "visible":
                        new_content[x][y] = self.get_new_seat_in_sight(x, y)
                    elif rules == "adjacent":
                        new_content[x][y] = self.get_new_seat(x, y)
                    continue
            if self.content == new_content:
                break
            self.content = new_content
        return self.get_occupied()

    def get_occupied(self):
        occupied = 0
        for arr in self.content:
            occupied += arr.count("#")
        return occupied

    def get_new_seat(self, target_x, target_y):
        occupied = 0
        target_char = self.content[target_x][target_y]
        for x in range(target_x - 1, target_x + 2):
            for y in range(target_y - 1, target_y + 2):
                # check if out of bounds
                if x < 0 or y < 0 or x > len(self.content) - 1 or y > len(self.content[0]) - 1:
                    continue
                if x == target_x and y == target_y:
                    continue
                char = self.content[x][y]
                if char == "#":
                    if target_char == "L":
                        return target_char
                    occupied += 1
        if target_char == "L" and occupied == 0:
            return "#"
        if target_char == "#" and occupied >= 4:
            return "L"
        return target_char

    def get_new_seat_in_sight(self, target_x, target_y):
        occupied = 0
        target_char = self.content[target_x][target_y]
        for x in range(-1, 2):
            for y in range(-1, 2):
                if x == 0 and y == 0:
                    continue
                delta = 1
                while True:
                    # check in all directions
                    tempx = (x * delta) + target_x
                    tempy = (y * delta) + target_y
                    # check if out of bounds
                    if tempx < 0 or tempy < 0 or tempx > len(self.content) - 1 or tempy > len(self.content[0]) - 1:
                        break
                    char = self.content[tempx][tempy]
                    if char != ".":
                        if char == "#":
                            occupied += 1
                        break
                    delta += 1

        if target_char == "L" and occupied == 0:
            return "#"
        if target_char == "#" and occupied >= 5:
            return "L"
        return target_char


area = Area(input)
start = time.time()

# bruteforce solution today, it issss what it isss
print("Part One : " + str(area.run("adjacent")))

# part 2
print("Part Two : " + str(area.run("visible")))

end = time.time()
print(f"Runtime of the program is {end - start} seconds")
