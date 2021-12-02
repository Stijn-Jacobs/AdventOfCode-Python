# Advent of code Year 2021 Day 2 solution
# Author = Stijn-Jacobs
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def move_ship(inp, use_aim):
    depth = 0
    aim = 0
    horizon_pos = 0
    for line in inp:
        split = line.split(" ")
        operator = split[0]
        amount = int(split[1])
        match operator:
            case "forward":
                horizon_pos += amount
                if use_aim:
                    depth += (aim * amount)
            case "up":
                if use_aim:
                    aim -= amount
                else:
                    depth -= amount
            case "down":
                if use_aim:
                    aim += amount
                else:
                    depth += amount
    return depth * horizon_pos


print("Part One : " + str(move_ship(input, False)))

print("Part Two : " + str(move_ship(input, True)))
