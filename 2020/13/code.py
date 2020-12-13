# Advent of code Year 2020 Day 13 solution
# Author = Stijn-Jacobs
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

busses = input[1].split(",")
estimate = int(input[0])

# part 1 specific
lowest, lowest_wait = -1, -1
for bus in busses:
    if bus != "x":
        time_to_wait = abs((estimate % int(bus)) - int(bus))
        if lowest == -1 or time_to_wait < lowest_wait:
            lowest = int(bus)
            lowest_wait = time_to_wait

print("Part One : " + str(lowest * lowest_wait))


def chinese_remainder_theorem(equations):
    t = 0
    P = 1
    for _, pi in equations:
        P *= pi

    for ai, pi in equations:
        ni = P // pi
        inv = pow(ni, -1, pi)
        t = (t + ai * ni * inv) % P
    return t


# part 2 specific
part_2 = []
for i, t in enumerate(busses):
    if t != 'x':
        part_2.append((-i, int(t)))

print("Part Two : " + str(chinese_remainder_theorem(part_2)))
