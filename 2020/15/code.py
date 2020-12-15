# Advent of code Year 2020 Day 15 solution
# Author = Stijn-Jacobs
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readline().rstrip()


# back at the bruteforce once again /shrug
def play_game(maximum):
    lastspoken = {}
    last = -1
    # startig words
    for index, num in enumerate(input.split(",")):
        lastspoken[int(num)] = index + 1
        last = int(num)

    # game itself
    i = len(input.split(",")) + 1
    for i in range(i, maximum + 1):
        if last not in lastspoken:
            lastspoken[last] = i - 1
            last = 0
        else:
            templast = lastspoken[last]
            lastspoken[last] = i - 1
            last = (i - 1) - templast
    return last


# part 1 specific code
print("Part One : " + str(play_game(2020)))

# part 2 specific code
print("Part Two : " + str(play_game(30000000)))
