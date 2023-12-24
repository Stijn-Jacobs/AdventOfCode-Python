# Advent of code Year 2023 Day 6 solution
# Author = Stijn-Jacobs
# Date = December 2023

import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

# extract all integers from input[0], and put them in a list
times = [int(s) for s in input[0].split() if s.isdigit()]
distances = [int(s) for s in input[1].split() if s.isdigit()]


def calc(tim, dist):
    sum = 1  # start with 1, so we can multiply
    for i in range(len(tim)):
        possibilities = 0
        for j in range(0, tim[i] + 1):
            if (tim[i] - j) * j > dist[i]:
                possibilities += 1

        sum *= possibilities

    return sum


def part1():
    return calc(times, distances)


def part2():
    # merge all times together as they where strings
    times_p2 = [int("".join([str(i) for i in times]))]
    distances_p2 = [int("".join([str(i) for i in distances]))]

    return calc(times_p2, distances_p2)


print(part1())
print(part2())
