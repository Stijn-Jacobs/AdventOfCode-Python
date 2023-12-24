# Advent of code Year 2023 Day 8 solution
# Author = Stijn-Jacobs
# Date = December 2023
import math

import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

# firstly read direction instructions
directions = input[0].replace("\n", "")

nodes = []

root_node = None


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


# First add all nodes
for i in input[2:]:
    nodes.append(Node(i.replace("\n", "").split(" = ")[0], None, None))


def find_node_by_value(value):
    for n in nodes:
        if n.value == value:
            return n
    return None


# create the tree, from the added nodes
for i in input[2:]:
    # find the node
    name = i.replace("\n", "").split(" = ")[0]
    node = find_node_by_value(name)
    children = i.replace("\n", "").split(" = ")[1].replace("(", "").replace(")", "").split(", ")
    node.left = find_node_by_value(children[0])
    node.right = find_node_by_value(children[1])

    if node.value == "AAA":
        root_node = node


def part1():
    # loop through instructions, until we hit node ZZZ
    global root_node
    node = root_node
    steps = 0
    while node.value != "ZZZ":
        dir = directions[steps % len(directions)]
        if dir == "L":
            node = node.left
        elif dir == "R":
            node = node.right

        steps += 1

    return steps


def part2():
    global nodes

    # gather all the starting nodes, that start with A
    starting_nodes = []
    for node in nodes:
        if node.value.endswith("A"):
            # we found a node that ends with A, now we need to find the path to the root node
            starting_nodes.append(node)

    lcm = []

    for node in starting_nodes:
        steps = 0
        while not node.value.endswith("Z"):
            dir = directions[steps % len(directions)]
            if dir == "L":
                node = node.left
            elif dir == "R":
                node = node.right

            steps += 1

        lcm.append(steps)

    return math.lcm(*lcm)


print(part1())
print(part2())
