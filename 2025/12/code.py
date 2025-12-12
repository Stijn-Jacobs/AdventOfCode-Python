# Advent of code Year 2025 Day 12 solution
# Author = Stijn-Jacobs
# Date = December 2025

from functools import cached_property

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


# region has a size, and the index + amount of how many presents it should fit
class Region:
    def __init__(self, width, height, amount):
        self.width = width
        self.height = height
        self.amount = amount
        self.data = [0 for _ in range(height)]  # each row is a bitmask

    def fits(self, present_masks, top, left):
        for i, mask in enumerate(present_masks):
            if self.data[top + i] & (mask << left):
                return False
        return True

    def place(self, present_masks, top, left):
        for i, mask in enumerate(present_masks):
            self.data[top + i] |= (mask << left)

    def remove(self, present_masks, top, left):
        for i, mask in enumerate(present_masks):
            self.data[top + i] ^= (mask << left)

    def __str__(self):
        return f"Region {self.width}: Size {self.height}, Amount {self.amount}"

def grid_to_masks(grid):
    masks = []
    for row in grid:
        mask = 0
        for cell in row:
            mask = (mask << 1) | cell
        masks.append(mask)
    return masks

# presents have a 3x3 boolean grid as data
class Present:
    def __init__(self, index, data):
        self.index = index
        self.data = [[cell == '#' for cell in row] for row in data]

    def __str__(self):
        grid_str = "\n".join("".join(row) for row in self.data)
        return f"Present {self.index}:\n{grid_str}"

    @cached_property
    def get_variants(self):
        variants = set()

        def rotate(grid):
            return [[grid[2 - c][r] for c in range(3)] for r in range(3)]

        def flip(grid):
            return [row[::-1] for row in grid]

        current = self.data
        for _ in range(4):
            variants.add(tuple(tuple(row) for row in current))
            current = rotate(current)

        current = flip(self.data)
        for _ in range(4):
            variants.add(tuple(tuple(row) for row in current))
            current = rotate(current)

        # convert to bitmasks
        return [grid_to_masks([list(row) for row in v]) for v in variants]


presents = []
regions = []

def parse_presents():
    index = 0
    cur_present = None

    for line in input:
        line = line.strip()
        if not line:
            continue

        if ":" in line:
            if cur_present:
                presents.append(Present(index, [row[:3] for row in cur_present]))
                index += 1
                cur_present = []

            name, grid_data = line.split(":")
            if name.isdigit():
                cur_present = []
        else:
            if len(line) >= 3:
                cur_present.append(line)

    if cur_present:
        presents.append(Present(index, [row[:3] for row in cur_present]))

def parse_regions():
    for line in input:
        line = line.strip()
        if not line or ":" not in line:
            continue

        if "x" in line.split(":")[0]:
            dimensions, numbers = line.split(":")
            width, height = map(int, dimensions.split("x"))
            values = list(map(int, numbers.strip().split()))

            regions.append(Region(width, height, values))


parse_presents()
parse_regions()

def solve(region, presents, placements=None, visualizer=None):
    if placements is None:
        placements = []

    # check if this area can even work, if we don't have 7 (number of cells in a present) free cells per present, it can't work
    if len(presents) * 7 > region.width * region.height:
        return None

    # if we don't have enough free space, return None already before doing any compute
    free = 0
    full_mask = (1 << region.width) - 1
    for row in region.data:
        free += bin(~row & full_mask).count("1")

    needed = sum(sum(cell for row in p.data for cell in row) for p in presents)

    if needed > free:
        return None

    if not presents:
        return placements

    present = presents[0]

    fh, fw = region.height, region.width

    for variant in present.get_variants:
        for r in range(fh - 3 + 1):
            for c in range(fw - 3 + 1):
                if region.fits(variant, r, c):
                    region.place(variant, r, c)
                    placements.append((variant, (r, c)))

                    result = solve(region, presents[1:], placements, visualizer)
                    if result:
                        return result

                    # Backtrack and reset the last placement
                    placements.pop()
                    region.remove(variant, r, c)

    return None

def part_1():
    can_fit = 0
    for r in regions:
        new_presents = []

        for index, amount in enumerate(r.amount):
            for _ in range(amount):
                new_presents.append(presents[index])

        placements = solve(r, new_presents)
        if placements is not None:
            can_fit += 1

    return can_fit

def part_2():
    return -1

print(part_1())
print(part_2())