# Advent of code Year 2021 Day 12 solution
# Author = Stijn-Jacobs
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

caves = {}


class Cave:
    def __init__(self, name):
        self.name = name
        self.connections = []

    def add_connection(self, connection):
        self.connections.append(connection)

    def __repr__(self):
        return str(self.name)


def load_caves():
    for line in input:
        split = line.strip().split("-")
        c1 = caves.get(split[0], Cave(split[0]))
        c2 = caves.get(split[1], Cave(split[1]))

        c1.add_connection(c2)
        c2.add_connection(c1)

        caves[split[0]] = c1
        caves[split[1]] = c2


def find_paths(curpath="start", small_caves_visited={}, allowed_twice=None):
    cur_cave = caves[curpath]
    if (curpath.islower() and curpath not in small_caves_visited) or allowed_twice:
        small_caves_visited[cur_cave.name] = small_caves_visited.get(cur_cave.name, 0) + 1
    paths = []
    if curpath == "end":
        paths.append(curpath)
    for con in cur_cave.connections:
        if con.name == "end":
            paths.append(curpath + ",end")
            continue
        if con.name.isupper() or small_caves_visited.get(con.name, 0) == 0 or (
                allowed_twice == con.name and small_caves_visited.get(con.name, 0) <= 1):
            for item in find_paths(con.name, small_caves_visited=small_caves_visited.copy(),
                                   allowed_twice=allowed_twice):
                paths.append(curpath + "," + item)
    return paths


def part2():
    # Get all possible double visitable caves, and combine all the results, in a a set so no dupes.
    lowercase_caves = set()
    for line in input:
        for split in line.strip().split("-"):
            if split.islower():
                lowercase_caves.add(split)
    lowercase_caves.remove("start")
    lowercase_caves.remove("end")

    connections = set()
    for lower in lowercase_caves:
        for item in find_paths(allowed_twice=lower):
            connections.add(item)
    return len(connections)


load_caves()

print("Part One : " + str(len(find_paths())))

print("Part Two : " + str(part2()))
