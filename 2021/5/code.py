# Advent of code Year 2021 Day 5 solution
# Author = Stijn-Jacobs
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def get_increase(x):
    return (x > 0) - (x < 0)


class FloorMap:
    def __init__(self):
        self.locations = {}

    def load_from_lines(self, inp, support_diagonal):
        for line in inp:
            split = line.split(" -> ")
            x1, y1 = list(map(int, split[0].strip().split(",")))
            x2, y2 = list(map(int, split[1].strip().split(",")))

            # Horizontal and vertical only
            if support_diagonal or (x1 == x2 or y1 == y2):
                x_inc, y_inc = get_increase(x2 - x1), get_increase(y2 - y1)
                while (x1, y1) != (x2 + x_inc, y2 + y_inc):
                    self.locations[(x1, y1)] = self.locations.get((x1, y1), 0) + 1
                    x1 += x_inc
                    y1 += y_inc

    def get_overlapping_sum(self):
        return sum(occurance >= 2 for occurance in self.locations.values())


part1floor = FloorMap()
part1floor.load_from_lines(input, False)

print("Part One : " + str(part1floor.get_overlapping_sum()))

part2floor = FloorMap()
part2floor.load_from_lines(input, True)

print("Part Two : " + str(part2floor.get_overlapping_sum()))
