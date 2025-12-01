# Advent of code Year 2025 Day 1 solution
# Author = Stijn-Jacobs
# Date = December 2025

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

def solution(count_all_0_positions=False):
    dial = 50
    pointed_up = 0

    for line in input:
        split = list(line.replace('\n', ''))
        direction = split.pop(0)

        value = int(''.join(split))

        old_dial = dial

        if direction == 'L':
            dial -= value
        elif direction == 'R':
            dial += value

        # Also count if reached 0 by going past it
        if count_all_0_positions:
            if direction == 'R':
                pointed_up += (old_dial + value) // 100
            else:
                if old_dial == 0:
                    pointed_up += value // 100
                elif value >= old_dial:
                    pointed_up += (value - old_dial) // 100 + 1
            dial %= 100
        else:
            dial %= 100
            if dial == 0:
                pointed_up += 1


    return pointed_up


print(solution())
print(solution(count_all_0_positions=True))