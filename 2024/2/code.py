# Advent of code Year 2024 Day 2 solution
# Author = Stijn-Jacobs
# Date = December 2024
from itertools import count

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

def parse_input(input):
    return [[int(i) for i in i.split(' ')] for i in input]

def get_diffs(line):
    return [line[j] - line[j + 1] for j in range(len(line) - 1)]

def is_valid_diff(diff_arr):
    return all([abs(diff) in range(1, 4) for diff in diff_arr]) and \
           (all(diff > 0 for diff in diff_arr) or all(diff < 0 for diff in diff_arr))

def solve1(input):
    diffs = [get_diffs(i) for i in parse_input(input)]
    return sum([is_valid_diff(diff_arr) for diff_arr in diffs])

def solve2(input):
    sum = 0

    for line in parse_input(input):
        for i in range(-1, len(line)):
            copy = line
            if i >= 0:  # remove element and check if valid that way
                copy = line[:i] + line[i + 1:]
            diff_arr = get_diffs(copy)
            if is_valid_diff(diff_arr):
                sum += 1
                break
    return sum

print(solve1(input))
print(solve2(input))