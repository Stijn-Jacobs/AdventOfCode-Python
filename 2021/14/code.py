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

    i = 0
    while i < steps:
        i += 1
        new = []
        prev = ""
        for char in starting:
            new += rules.get(prev + char, "")
            new += char
            prev = char
        starting = new

    counter = Counter(starting)
    counter_values = counter.values()
    return max(counter_values) - min(counter_values)


print("Part One : " + str(template_score_after_steps(input, 10)))

print("Part Two : " + str(template_score_after_steps(input, 40)))
