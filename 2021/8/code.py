# Advent of code Year 2021 Day 8 solution
# Author = Stijn-Jacobs
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def part1(inp):
    appearance = 0
    for line in inp:
        output = line.split(" | ")[1].strip()
        for split in output.split(" "):
            # Identify numbers by section count
            if len(split) in [2, 4, 3, 7]:
                appearance += 1
    return appearance


print("Part One : " + str(part1(input)))

print("Part Two : " + str(None))
