# Advent of code Year 2020 Day 7 solution
# Author = Stijn-Jacobs
# Date = December 2020

import re

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

bags = {}


class Bag:
    def __init__(self, color, contains):
        self.color = color
        self.contains = contains

    # checks if this bag, or any bags this bag contains, contains the specified bag
    def check_if_can_contain(self, target_bag):
        for containing_bag in self.contains:
            # Check if bag itself is the target bag, or any sub bags is the target bag
            if containing_bag[1] == target_bag or bags[containing_bag[1]].check_if_can_contain(target_bag):
                return True
        return False

    # gets the amount of bags this bag contains, including sub bags
    def get_contains(self, count_itself=False):
        if len(self.contains) == 0:
            return 1
        else:
            sum = 0
            for containing_bag in self.contains:
                sum += (bags[containing_bag[1]].get_contains(count_itself=True) * int(containing_bag[0]))
            return sum + 1 if count_itself else sum  # + 1 for itself


for line in input:
    line_regexed = re.findall("(\d)*?\s?(\w*\s\w*)\sbags?", line)
    subject_bag_color = line_regexed[0][1]
    line_regexed.remove(line_regexed[0])
    if line_regexed[0][1] is not None:
        subject_bag = Bag(subject_bag_color, line_regexed if line_regexed[0][1] != "no other" else [])
        bags[subject_bag_color] = subject_bag


# part 1 code
part_1_sum = 0
for bag in bags:
    if bags[bag].check_if_can_contain("shiny gold"):
        part_1_sum += 1

print("Part One : " + str(part_1_sum))

# part 2 code
print("Part Two : " + str(bags["shiny gold"].get_contains(False)))
