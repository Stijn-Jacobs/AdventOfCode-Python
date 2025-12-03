# Advent of code Year 2025 Day 3 solution
# Author = Stijn-Jacobs
# Date = December 2025
from collections import Counter
from itertools import combinations
from os.path import split
import re

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def solution(max_turned_on=2):
    sol = 0
    for bank in input:
        digits = list(map(int, re.findall(r'\d', bank)))
        k = max_turned_on

        stack = []
        to_remove = len(digits) - k

        for d in digits:
            while to_remove > 0 and stack and stack[-1] < d:
                stack.pop()
                to_remove -= 1
            stack.append(d)

        best_subsequence = stack[:k]

        number = int("".join(map(str, best_subsequence)))
        sol += number

    return sol


print(solution())
print(solution(max_turned_on=12))