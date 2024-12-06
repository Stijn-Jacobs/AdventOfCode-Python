# Advent of code Year 2024 Day 1 solution
# Author = Stijn-Jacobs
# Date = December 2024
from itertools import count

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

def parse_lists(input):
    lists = [[], []]
    for i in input:
        split = [int(x) for x in i.split('   ')]
        [lists[i].append(split[i]) for i in range(len(split))]

    return lists

def solve1(input):
    sum = 0

    lists = parse_lists(input)

    [list.sort() for list in lists]

    for i in range(len(lists[0])):
        sum += abs(lists[1][i] - lists[0][i])

    return sum

def solve2(input):
    sum = 0

    lists = parse_lists(input)

    for i in range(len(lists[0])):
        sum += lists[0][i] * lists[1].count(lists[0][i])

    return sum

print(solve1(input))

print(solve2(input))