# Advent of code Year 2021 Day 7 solution
# Author = Stijn-Jacobs
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readline()


def find_least_movements_position(inp, exponential=False):
    arr = list(map(int, inp.split(",")))
    fuels_spent_arr = []

    for target in range(min(arr), max(arr)):
        fuel_spent = 0
        for num in arr:
            if exponential:
                fuel_spent += abs(num - target) * (abs(num - target) + 1) // 2
            else:
                fuel_spent += abs(num - target)

        fuels_spent_arr.append(fuel_spent)

    return min(fuels_spent_arr)


print("Part One : " + str(find_least_movements_position(input)))

print("Part Two : " + str(find_least_movements_position(input, True)))
