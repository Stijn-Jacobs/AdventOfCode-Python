# Advent of code Year 2024 Day 2 solution
# Author = Stijn-Jacobs
# Date = December 2024
import re

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

def format_input(input):
    return ''.join(input).replace('\n', '')

def solve_mul(raw):
    res = raw[4:-1].split(',')
    return int(res[0]) * int(res[1])

def solve1(input):
    return sum([solve_mul(res) for res in re.findall('(mul\([0-9]*,[0-9]*\))', format_input(input))])

def solve2(input):
    enabled = True
    sum = 0
    for res in re.findall('(mul\([0-9]*,[0-9]*\)|don\'t\(\)|do\(\))', format_input(input)):
        if res == 'don\'t()':
            enabled = False
        elif res == 'do()':
            enabled = True
        elif enabled:
            sum += solve_mul(res)

    return sum

print(solve1(input))
print(solve2(input))