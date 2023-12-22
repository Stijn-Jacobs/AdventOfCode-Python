# Advent of code Year 2023 Day 1 solution
# Author = Stijn-Jacobs
# Date = December 2023

import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


class Card:
    # constructor
    def __init__(self, num, winning, numbers):
        self.num = num
        self.winning = winning
        self.numbers = numbers


# firstly convert to card model
cards = []

for i in range(len(input)):
    numbers_split = input[i].replace("\n", "").split(": ")[1].split(" | ")

    arr = [[int(c) for c in r.removeprefix(" ").replace("  ", " ").split(" ")] for r in
           [numbers_split[0], numbers_split[1]]]

    cards.append(Card(i + 1, arr[0], arr[1]))

# sort by number
cards.sort(key=lambda x: x.num)

# improve performance by caching
scratch_cache = {}


def part2():
    return sum([scratch_recursive(cards[i]) for i in range(0, len(cards))])


def scratch_recursive(card):
    scratch_amount = scratch(card)
    if scratch_amount == 0:
        return 1
    return sum([scratch_recursive(cards[i]) for i in range(card.num, card.num + scratch_amount)]) + 1


def scratch(card):
    if card.num in scratch_cache:
        return scratch_cache[card.num]

    sum = 0
    # check how many numbers are in the winning list
    for number in card.numbers:
        if number in card.winning:
            sum += 1

    scratch_cache[card.num] = sum
    return sum


def part1():
    total_sum = 0
    for card in cards:
        val = scratch(card)
        if val >= 1:
            total_sum += 2 ** (val - 1)

    return total_sum


print(part1())
print(part2())
