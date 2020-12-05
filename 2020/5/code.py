# Advent of code Year 2020 Day 5 solution
# Author = Stijn-Jacobs
# Date = December 2020

import math

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

rows = 128
columns = 8


def change_bounds(upper, bounds):
    if upper:
        return bounds[0], math.floor(sum(bounds) / 2)
    else:
        return math.ceil(sum(bounds) / 2), bounds[1]


class Seat:
    def __init__(self, content):
        self.seat_id = -1
        self.content = content
        self.location = (-1, -1)

    def find_seat(self):
        x_bounds = (0, rows - 1)
        y_bounds = (0, columns - 1)

        for char in self.content:
            if char == "F" or char == "B":  # rows
                x_bounds = change_bounds(char == "F", x_bounds)

            if char == "L" or char == "R":  # colums
                y_bounds = change_bounds(char == "L", y_bounds)

        self.seat_id = (x_bounds[0] * 8) + y_bounds[0]
        self.location = x_bounds[0], y_bounds[0]
        return self.location


# Part 1 specific code
seats = []
max_seat_id = -1
for line in input:
    seat = Seat(line)
    seats.append(seat)
    seat.find_seat()
    if seat.seat_id > max_seat_id:
        max_seat_id = seat.seat_id

# part 2 specific
seats.sort(key=lambda seat: seat.location)

max_seat_x = max(seat.location[0] for seat in seats)
y_index = 0
missing_seat_id = -1
for s in seats:
    if s.location[0] == 1 or s.location[0] == max_seat_x:  # exclude first and last row
        continue

    if s.location[1] is not y_index:
        missing_seat_id = ((s.location[0] if y_index != columns - 1 else s.location[0] - 1) * 8) + y_index
        y_index = s.location[1] + 1
    else:
        y_index += 1

    if y_index >= columns:
        y_index -= columns

print("Part One : " + str(max_seat_id))

print("Part Two : " + str(missing_seat_id))
