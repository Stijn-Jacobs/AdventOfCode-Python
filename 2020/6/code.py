# Advent of code Year 2020 Day 6 solution
# Author = Stijn-Jacobs
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


class Group:
    def __init__(self):
        self.answers = []

    def get_anyone_yes_answers(self):
        yes_answers = []
        for answer in self.answers:
            for char in answer:
                if char not in yes_answers:
                    yes_answers.append(char)

        return yes_answers

    def get_everyone_yes_answers(self):
        yes_answers = self.get_anyone_yes_answers()
        disqualified = []
        for answer_char in yes_answers:
            for answer in self.answers:
                if answer_char not in answer and answer_char not in disqualified:
                    disqualified.append(answer_char)

        # remove the disqualified chars
        for remove in disqualified:
            yes_answers.remove(remove)

        return yes_answers


groups = []

current = Group()
groups.append(current)
for line in input:
    if line != "\n":
        current.answers.append(line.rstrip())
    else:
        current = Group()
        groups.append(current)

# Part 1 specific code
# sums up all the unique yes answers of each group
part_one_sum = sum((len(group.get_anyone_yes_answers()))
                   for group in groups)

print("Part One : " + str(part_one_sum))

# Part 2 specific
part_two_sum = sum((len(group.get_everyone_yes_answers()))
                   for group in groups)

print("Part Two : " + str(part_two_sum))
