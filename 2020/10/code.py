# Advent of code Year 2020 Day 10 solution
# Author = Stijn-Jacobs
# Date = December 2020

from collections import Counter

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

# convert to int list
input = [int(i) for i in input]

# part 1 specific

def part1(adapters):
    adapters.sort()
    adapters.insert(0, 0)  # starting port
    differences = [j - i for i, j in zip(adapters[:-1], adapters[1:])]
    differences.append(3)  # add 3 for the last
    return differences.count(1) * differences.count(3)


inp = input.copy()
print("Part One : " + str(part1(inp)))


# part 2 specific code

class Arrangement:
    def __init__(self, contents):
        self.contents = contents
        self.contents.insert(0, 0)  # starting port
        self.contents.append(max(self.contents) + 3)
        self.contents.sort()

    def get_valid_arrangements_count(self):
        c = Counter({0: 1})
        for x in self.contents:
            c[x + 1] += c[x]
            c[x + 2] += c[x]
            c[x + 3] += c[x]
        return c[max(self.contents) + 3]


arr = Arrangement(input)
print("Part Two : " + str(arr.get_valid_arrangements_count()))
