# Advent of code Year 2020 Day 1 solution
# Author = Stijn-Jacobs
# Date = December 2020

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

for first in input:
    for second in input:
        sum = int(first) + int(second)
        for third in input:
            if sum + int(third) == 2020:
                secondOutput = int(first) * int(second) * int(third)
                break
        if sum == 2020:
            firstOutput = (int(first) * int(second))

print("Part One : "+ str(firstOutput))
print("Part Two : "+ str(secondOutput))