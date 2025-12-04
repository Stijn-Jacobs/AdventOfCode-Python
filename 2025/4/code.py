# Advent of code Year 2025 Day 4 solution
# Author = Stijn-Jacobs
# Date = December 2025

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

# convert the input to 2d array
input_array = []
for line in input:
    input_array.append(list(line.strip()))

debug = False

def part_1():
    return find_removeable_count()[1]

def part_2():
    total = 0
    while True:
        res = find_removeable_count()
        total += res[1]

        # remove the found removable characters
        for x, y in res[0]:
            input_array[x][y] = '.'

        if res[1] == 0:
            break
    return total

def find_removeable_count():
    total = 0
    removable = []
    for x in range(len(input_array)):
        for y in range(len(input_array[x])):
            chars = {}

            if input_array[x][y] != '@':
                print("0", end="") if debug else None
                continue

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(input_array) and 0 <= ny < len(input_array[x]):
                        char = input_array[nx][ny]
                        if char not in chars:
                            chars[char] = 0
                        chars[char] += 1

            if '@' not in chars or chars['@'] < 4:
                total += 1
                removable.append((x, y))
                print("1", end="") if debug else None
            else:
                print("0", end="") if debug else None
        print() if debug else None
    return removable, total

print(part_1())
print(part_2())