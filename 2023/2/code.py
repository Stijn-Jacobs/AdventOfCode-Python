# Advent of code Year 2023 Day 1 solution
# Author = Stijn-Jacobs
# Date = December 2023

import math

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def part2():
    sum = 0
    for line in input:
        # extract game id
        map = {}

        for row in line.split(": ")[1].split("; "):
            for throw in row.split(", "):
                split = throw.split(" ")
                color = split[1].replace("\n", "")
                if map.get(color) is None or int(split[0]) > int(map[color]):
                    map[color] = int(split[0])

        # multiple all values
        sum += math.prod([v for k, v in map.items()])
    return sum


def part1():
    total = 0
    for line in input:
        # extract game id
        game_id = int(line.split(": ")[0].replace("Game ", ""))

        valid = True
        for row in line.split(": ")[1].split("; "):
            for throw in row.split(", "):
                split = throw.split(" ")
                color = split[1].replace("\n", "")

                if color == "red" and int(split[0]) > 12:
                    valid = False
                    break

                if color == "green" and int(split[0]) > 13:
                    valid = False
                    break

                if color == "blue" and int(split[0]) > 14:
                    valid = False
                    break

        if valid:
            total += game_id

    return total


print(part1())
print(part2())
