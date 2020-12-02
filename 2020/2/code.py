# Advent of code Year 2020 Day 2 solution
# Author = Stijn-Jacobs
# Date = December 2020

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


def validate_password(password, index, targetChar):
    if len(password) > index and password[index - 1] == targetChar:
        return True
    return False


sum = 0
sumTwo = 0
for line in input:
    mainSplit = line.split(": ")
    password = mainSplit[1]
    secondSplit = mainSplit[0].split(" ")
    targetChar = secondSplit[1]
    amountSplit = secondSplit[0].split("-")
    minAmount = int(amountSplit[0])
    maxAmount = int(amountSplit[1])
    occurs = password.count(targetChar)
    if minAmount <= occurs <= maxAmount:
        sum += 1

    # part 2
    firstValid = validate_password(password, minAmount, targetChar)
    secondValid = validate_password(password, maxAmount, targetChar)
    if (firstValid and not secondValid) or (secondValid and not firstValid):
        sumTwo += 1


print("Part One : " + str(sum))
print("Part Two : " + str(sumTwo))
