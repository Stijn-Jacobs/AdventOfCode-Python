# Advent of code Year 2021 Day 3 solution
# Author = Stijn-Jacobs
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def part1(inp):
    gamma = ""
    epsilion = ""
    for index in range(0, len(inp[0]) - 1):
        char = str(most_common_char(inp, index, False))
        gamma += char
        epsilion += '1' if char == '0' else '0'
    return int(gamma, 2) * int(epsilion, 2)


def find_remainding(input, reversed):
    new = input.copy()
    for index in range(0, len(input[0]) - 1):
        char = most_common_char(new, index, reversed)
        temp = new.copy()
        for line in new:
            if line[index] != str(char):
                temp.remove(line)
        new = temp
        if len(new) == 1:
            return new[0]
    return None


def part2(inp):
    oxygen = int(find_remainding(inp, False), 2)
    co2 = int(find_remainding(inp, True), 2)
    return oxygen * co2


def most_common_char(inp, index, reversed):
    zero_count = 0
    for line in inp:
        char = line[index]
        if char == '0':
            zero_count += 1

    if reversed:
        return 0 if zero_count <= len(inp) / 2 else 1
    else:
        return 0 if zero_count > len(inp) / 2 else 1


print("Part One : " + str(part1(input)))

print("Part Two : " + str(part2(input)))
