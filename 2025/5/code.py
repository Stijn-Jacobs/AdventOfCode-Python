# Advent of code Year 2025 Day 5 solution
# Author = Stijn-Jacobs
# Date = December 2025

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

fresh_ranges = []
ing = []


for line in input:
    if '-' in line:
        fresh_ranges += [list(map(int, line.strip().split('-')))]
    elif line != '\n':
        ing += [int(line.strip())]


def part_1():
    fresh = 0

    for i in ing:
        still_fresh = False
        for r in fresh_ranges:
            if r[0] <= i <= r[1]:
                still_fresh = True
                break
        if still_fresh:
            fresh += 1

    return fresh

def merge_ranges(range1, range2):
    # Returns merged range if they overlap, None otherwise
    if range1[0] <= range2[1] + 1 and range1[1] >= range2[0] - 1:
        return min(range1[0], range2[0]), max(range1[1], range2[1])
    return None


def part_2():
    ranges = set()

    for r in fresh_ranges:
        current = (r[0], r[1])
        ranges.add(current)

    # Keep merging until no changes
    while True:
        fully_merged = False
        new_ranges = set()
        remaining = ranges.copy()

        while remaining:
            current = remaining.pop()
            merged_something = False

            for other in remaining:
                merged_range = merge_ranges(current, other)
                if merged_range:
                    new_ranges.add(merged_range)
                    remaining.remove(other)
                    fully_merged = True
                    merged_something = True
                    break

            if not merged_something:
                new_ranges.add(current)

        if not fully_merged:
            break

        ranges = new_ranges

    # sum up the unique ranges
    return sum([abs(x[0] - x[1] - 1) for x in ranges])


print(part_1())
print(part_2())