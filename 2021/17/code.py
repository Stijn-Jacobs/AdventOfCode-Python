# Advent of code Year 2021 Day 17 solution
# Author = Stijn-Jacobs
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readline()

target_area = [int(''.join(i for i in char if i.isdigit() or i == "-")) for char in
               input.split(": ")[1].replace(", ", "..").split("..")]


def test_if_valid(vel_x, vel_y):
    x, y = 0, 0
    while x <= max(target_area[:2]) and y >= min(target_area[2:3]):
        # Check if in target currently
        if (target_area[0] <= x <= target_area[1]
                and target_area[2] <= y <= target_area[3]):
            return True
        x += vel_x
        y += vel_y
        if vel_x > 0:
            vel_x -= 1
        elif vel_x < 0:
            vel_x += 1
        vel_y -= 1
    return False


def part2():
    valid = []
    for y in range(min(target_area[2:3]), abs(min(target_area[2:3]))):
        for x in range(0, max(target_area[:2]) + 1):
            if test_if_valid(x, y):
                valid.append((x, y))
    return len(valid)


print("Part One : " + str(sum(range(abs(min([int(target_area[2]), int(target_area[3])]))))))

print("Part Two : " + str(part2()))
