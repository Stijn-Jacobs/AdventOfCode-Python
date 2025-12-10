# Advent of code Year 2025 Day 8 solution
# Author = Stijn-Jacobs
# Date = December 2025
import math
from itertools import combinations

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

boxes = []

class Box:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.connections = set()

    # string representation
    def __repr__(self):
        return f"Box({self.x}, {self.y}, {self.z})"

    def get_all_connected(self):
        visited = set()
        def dfs(current_box):
            for connected_box in current_box.connections:
                if connected_box not in visited:
                    visited.add(connected_box)
                    dfs(connected_box)
        dfs(self)
        return visited

    def connect(self, box):
        self.connections.add(box)
        box.connections.add(self)

for line in input:
    x, y, z = map(int, line.strip().split(','))
    boxes.append(Box(x, y, z))

# get the sizes of all circuits in this list of boxes
def get_circuit_sizes(boxes):
    circuits = []
    visited = set()
    for b in boxes:
        if b in visited:
            continue

        connected = b.get_all_connected()
        visited.update(connected)
        circuits.append(connected)

    return circuits

def connect_close_boxes(boxes, closest_count=math.inf, connect_until_single_circuit=False) -> tuple:
    combs = combinations(boxes, 2)

    # get the distances between these combinations, store them in a list of tuples (distance, box_a, box_b)
    distances = []
    for box_a, box_b in combs:
        distance = math.sqrt((box_a.x - box_b.x) ** 2 + (box_a.y - box_b.y) ** 2 + (box_a.z - box_b.z) ** 2)
        distances.append((distance, box_a, box_b))

    # sort the distances, smallest first
    distances.sort(key=lambda x: x[0])

    if connect_until_single_circuit:
        for c in distances:
            c[1].connect(c[2])

            # to optimize this, if all boxes have at least 1 connection, if not, we can assume there is no single circuit.
            # drastically increasing the performance
            if all(len(b.connections) > 0 for b in boxes):
                circuits = get_circuit_sizes(boxes)

                if len(circuits) == 1:
                    return boxes, (c[1], c[2])
        return None, None # should not happen

    # apply the found connections.
    for c in distances[:closest_count]:
        c[1].connect(c[2])

    return boxes, None # no need to return the latest for part 1

def part_1():
    circuits = get_circuit_sizes(connect_close_boxes(boxes.copy(), 1000)[0])

    # sort the circuits by length of their set, so we can get the top three
    circuits.sort(key=lambda box: len(box), reverse=True)

    return math.prod([len(x) for x in circuits[0:3]])

def part_2():
    last = connect_close_boxes(boxes.copy(), connect_until_single_circuit=True)[1]

    return last[0].x * last[1].x

print(part_1())
print(part_2())