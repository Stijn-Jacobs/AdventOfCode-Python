# Advent of code Year 2020 Day 14 solution
# Author = Stijn-Jacobs
# Date = December 2020

import re
from itertools import product

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def mask_decimal(mask, decimal):
    binary = bin(int(decimal))[2:]
    if len(mask) > len(binary):
        binary = binary.rjust(len(mask), '0')
    binary = "".join(x if y == 'X' else y for x, y in zip(str(binary), mask))
    return int(binary, 2)


def mask_decimal_with_floating(mask, decimal):
    binary = bin(int(decimal))[2:]
    # extend binary with leading 0's, otherwise out of bounds
    if len(mask) > len(binary):
        binary = binary.rjust(len(mask), '0')
    x_indices = [idx for idx, ch in enumerate(mask) if ch == "X"]
    bit_combinations = product(range(2), repeat=len(x_indices))
    combos = []
    # first apply the static bits
    comb = list("".join("1" if y == '1' else x for x, y in zip(str(binary), mask)))
    for bit in bit_combinations:
        comb = list(comb)
        # apply transformations of current bit conbination
        for bit, idx in zip(bit, x_indices):
            comb[idx] = bit
        comb = [str(i) for i in comb]
        comb = "".join(comb)
        combos.append(comb)
    return [int(comb, 2) for comb in combos]


class Program:
    def __init__(self, program):
        self.program = program

    def run(self, version):
        mask = None
        reg = {}
        for instruction in self.program:
            split = instruction.split(" = ")
            if split[0] == "mask":
                mask = split[1].rstrip()
                continue
            memaddr = re.findall("(?<=\[).+?(?=\])", split[0])[0]
            if version == 1:
                reg[memaddr] = mask_decimal(mask, int(split[1]))
            else:
                for num in mask_decimal_with_floating(mask, memaddr):
                    reg[num] = int(split[1])
        return sum(reg.values())


pro = Program(input)
print("Part One : " + str(pro.run(version=1)))

print("Part Two : " + str(pro.run(version=2)))
