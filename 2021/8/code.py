# Advent of code Year 2021 Day 8 solution
# Author = Stijn-Jacobs
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Array which returns the corresponding number when given a character array of displaying segments.
chars_to_numbers = {"abcefg": 0,
                    "cf": 1,
                    "acdeg": 2,
                    "acdfg": 3,
                    "bcdf": 4,
                    "abdfg": 5,
                    "abdefg": 6,
                    "acf": 7,
                    "abcdefg": 8,
                    "abcdfg": 9}


def part1(inp):
    appearance = 0
    for line in inp:
        output = line.split(" | ")[1].strip()
        for split in output.split(" "):
            # Identify numbers by section count
            if len(split) in [2, 4, 3, 7]:
                appearance += 1
    return appearance


class ShuffledSignal:
    def __init__(self):
        # Each shuffeled signal(value) can be every output signal(key)
        self.possibilities = dict(zip([c for c in chars], [chars.copy() for i in range(0, 7)]))
        self.decoded = dict(zip([c for c in chars], [None for x in range(0, 7)]))

    def decode_code(self, code):
        decoded = ""
        for char in code:
            decoded += self.decoded[char]
        decoded = list(decoded)
        decoded.sort()
        decoded = "".join(decoded)

        return chars_to_numbers[decoded]

    # Returns true when every part of display is properly connected
    def process_valid_code(self, decode):
        # With given string, filters out if a wire match is not longer possible
        if len(decode) == 7:
            # Character represents an 8, can't filter anything out
            return
        elif len(decode) == 2:
            # Char represents a 1
            self.remove_posibilities_multiple(['a', 'b', 'd', 'e', 'g'], decode)
        elif len(decode) == 4:
            # Char represents a 4
            self.remove_posibilities_multiple(['a', 'e', 'g'], decode)
        elif len(decode) == 3:
            # Char represents a 7
            self.remove_posibilities_multiple(['b', 'd', 'e', 'g'], decode)

        # Discard by comparing 6 and 9 and 0
        elif len(decode) == 6:
            self.remove_other_multiple(['a', 'b', 'f', 'g'], decode)
        # Discard by comparing 5, 3 and 2
        elif len(decode) == 5:
            self.remove_other_multiple(['a', 'd', 'g'], decode)

        return self.update_confirmed()

    # Checks and see if 1 of the possiblities only has 1 left, so we can remove it from the rest of the arrays.
    # Returns wether or not all characters have 1 possibility left
    def update_confirmed(self):
        size = -1
        old_size = 0
        while size != old_size:
            temp = self.possibilities.copy()
            old_size = size
            size = sum([len(val) for val in temp.values()])
            for item in temp:
                if len(temp[item]) == 1:
                    fro = chars.copy()
                    fro.remove(item)
                    self.remove_posibilities_multiple(fro, temp[item][0])

        # check if every display has 1 possible matching cable left
        succes = True
        for item in self.possibilities.values():
            if len(item) > 1:
                succes = False

        if succes:
            # Setup decoded dict so we can easily decrypt the code
            temp = self.decoded.copy()
            for val in zip(self.possibilities.keys(), self.possibilities.values()):
                temp[val[1][0]] = val[0]
            self.decoded = temp
        return succes

    # Removes everything for each character int ouput_arr except when it is in the keep array
    def remove_other_multiple(self, output_arr, keep):
        for item in output_arr:
            self.remove_other(item, keep)

    def remove_other(self, output, keep):
        arr = self.possibilities[output]
        for item in arr:
            if item not in keep:
                arr.remove(item)

    # Removes every item from each item in output array that is in the remove_arr
    def remove_posibilities_multiple(self, output_arr, remove_arr):
        for item in output_arr:
            self.remove_posibilities(item, remove_arr)

    def remove_posibilities(self, output, remove_arr):
        arr = self.possibilities[output]
        for item in remove_arr:
            if item in arr:
                arr.remove(item)


def part2(inp):
    sum = 0
    for line in inp:
        sum += decrypt_line(line)
    return sum


def decrypt_line(line):
    sig = ShuffledSignal()
    split = line.strip().split(" | ")
    for item in split[0].split(" "):
        if sig.process_valid_code(item):
            break
    code = ""
    for item in split[1].split(" "):
        code += str(sig.decode_code(item))
    return int(code)


print("Part One : " + str(part1(input)))

print("Part Two : " + str(part2(input)))
