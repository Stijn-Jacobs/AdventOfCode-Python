# Advent of code Year 2021 Day 1 solution
# Author = Stijn-Jacobs
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def part1(inp):
    prev = None
    increased_counter = 0
    for inp in inp:
        if prev and int(inp) > int(prev):
            increased_counter += 1
        prev = inp
    return increased_counter


def part2(inp):
    index = 0
    # Convert all strings to int
    inp = list(map(int, inp))
    increased_counter = 0
    prev_avg = None
    while index + 2 < len(inp):
        # Calc average
        avg = sum(inp[index:index + 3]) / 3
        if prev_avg and avg > prev_avg:
            increased_counter += 1
        prev_avg = avg
        index += 1
    return increased_counter


print("Part One : " + str(part1(input)))

print("Part Two : " + str(part2(input)))
