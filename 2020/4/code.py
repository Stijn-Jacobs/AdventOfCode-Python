# Advent of code Year 2020 Day 4 solution
# Author = Stijn-Jacobs
# Date = December 2020

import re

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

# Corrects the input, by splitting on each empty line
correctInput = []
line = ""
for cur in input:
    line += ("" if line == "" else " ") + cur.rstrip()
    if cur == "\n":
        correctInput.append(line.rstrip())
        line = ""


def validate_height(height):
    found_letters = re.search("([a-z])+", height)
    found_numbers = re.search("([0-9])+", height)
    if found_numbers is None or found_letters is None:
        return False

    found_numbers = int(found_numbers.group())
    found_letters = found_letters.group()
    if found_letters == "cm":
        if 150 <= found_numbers <= 193:
            return True
    elif found_letters == "in":
        if 59 <= found_numbers <= 76:
            return True
    return False


class Passport:
    def __init__(self, contents):
        self.contents = dict((x.strip(), y.strip())
                             for x, y in (element.split(':')
                                          for element in contents.split(' ')))

    def valid_simple(self, required_fields):
        for field in required_fields:
            if field not in self.contents:
                return False
        return True

    def valid(self):
        con = self.contents
        if "byr" not in con or not (1920 <= int(con["byr"]) <= 2002):
            return False

        if "iyr" not in con or not (2010 <= int(con["iyr"]) <= 2020):
            return False

        if "eyr" not in con or not (2020 <= int(con["eyr"]) <= 2030):
            return False

        if "hgt" not in con or not validate_height(con["hgt"]):
            return False

        if "hcl" not in con or not re.search("#([0-9a-f]){6}", con["hcl"]):
            return False

        if "ecl" not in con or con["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
            return False

        if "pid" not in con or not re.search("^(([0-9]){9})$", con["pid"]):
            return False

        return True


passports = []

# import all passports
for entry in correctInput:
    passports.append(Passport(entry))

# Part 1 specific code
required_fields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
valid_passwords_part_1 = 0
for passport in passports:
    if passport.valid_simple(required_fields):
        valid_passwords_part_1 += 1

print("Part One : " + str(valid_passwords_part_1))

# part 2 specific code
valid_passwords_part_2 = 0
for passport in passports:
    if passport.valid():
        valid_passwords_part_2 += 1


print("Part Two : " + str(valid_passwords_part_2))
