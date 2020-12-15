# Advent of code Year 2020 Day 15 solution
# Author = Stijn-Jacobs
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readline().rstrip()


# back at the bruteforce once again /shrug
def play_game(maximum):
    lastspoken = {}
    mem = {}
    last = -1

    for index, num in enumerate(input.split(",")):
        lastspoken[int(num)] = index + 1
        last = int(num)
        if last in mem:
            mem[last] += 1
        else:
            mem[last] = 1
    i = len(input.split(",")) + 1
    while i <= maximum:
        if last not in mem or last in mem and mem[last] == 1:
            lastspoken[last] = i - 1
            last = 0
        else:
            lastspk = lastspoken[last]
            lastspoken[last] = i - 1
            last = abs((i - 1) - lastspk)

        if last in mem:
            mem[last] += 1
        else:
            mem[last] = 1

        i += 1
    return last


# part 1 specific code
print("Part One : " + str(play_game(2020)))

# part 2 specific code
print("Part Two : " + str(play_game(30000000)))
