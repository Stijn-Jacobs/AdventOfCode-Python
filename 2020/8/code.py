# Advent of code Year 2020 Day 8 solution
# Author = Stijn-Jacobs
# Date = December 2020
from computer import Computer

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

# part 1  specific code
computer = Computer(input)
computer.can_only_run_instruction_once = True
computer.start()

print("Part One : " + str(computer.accumulator))

# part 2 specific code
part_2_accumulator = -1
for instr in input:
    if "jmp" in instr or "nop" in instr:
        instructions_copy = input.copy()
        index = instructions_copy.index(instr)
        value = instructions_copy[index]

        # replace current instruction instruction
        instructions_copy[index] = value.replace("jmp" if "jmp" in instr else "nop", "nop" if "jmp" in instr else "jmp")
        computer = Computer(instructions_copy)
        computer.can_only_run_instruction_once = True
        if computer.start() == 0:  # check if error code = normal stop
            part_2_accumulator = computer.accumulator
            break

print("Part Two : " + str(part_2_accumulator))
