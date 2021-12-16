# Advent of code Year 2021 Day 14 solution
# Author = Stijn-Jacobs
# Date = December 2021

from collections import Counter

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def get_polymer_input(inp):
    starting = inp[0].strip()
    rules_dict = {}
    for rule in inp[2:]:
        split = rule.strip().split(" -> ")
        rules_dict[split[0]] = split[1]
    return starting, rules_dict


def template_score_after_steps(inp, steps):
    starting, rules = get_polymer_input(inp)

    pairs = dict(zip([starting[i] + starting[i + 1] for i in range(0, len(starting) - 1)],
                     [1 for _ in range(0, len(starting) - 1)]))
    characters = dict()
    for char in starting:
        characters[char] = characters.get(char, 0) + 1

    i = 0
    while i < steps:
        i += 1
        copy = pairs.copy()
        for pair in copy:
            to_add = rules[pair]
            if to_add:
                count = copy[pair]
                # Remove pair since we gonna add something in the middle
                pairs[pair] = pairs.get(pair, 0) - count

                pairs[pair[0] + to_add] = pairs.get(pair[0] + to_add, 0) + count
                pairs[to_add + pair[1]] = pairs.get(to_add + pair[1], 0) + count
                characters[to_add] = characters.get(to_add, 0) + count

    values = characters.values()
    return max(values) - min(values)


print("Part One : " + str(template_score_after_steps(input, 10)))

print("Part Two : " + str(template_score_after_steps(input, 40)))
