# Advent of code Year 2022 Day 1 solution
# Author = Stijn-Jacobs
# Date = December 2021

import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.read()

newArr = []
for i in np.char.split(np.array(input), sep='\n\n').tolist():
    newArr.append([int(numeric_string) for numeric_string in i.split('\n')])
sums = [sum(sublist) for sublist in newArr]

print("Part One : " + str(max(sums)))
sums = np.sort(sums)
print("Part Two : " + str(sum(sums[-3:])))
