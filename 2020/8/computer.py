class Computer:
    def __init__(self, instructions):
        self.ram = []
        self.pointer = 0
        self.accumulator = 0
        self.instructions = instructions

        # index of instructions already run
        self.run_history = []
        self.can_only_run_instruction_once = False

    def start(self):
        while self.pointer < len(self.instructions):
            if self.run():
                return 99  # 99 is run again error code
        return 0  # 0 is normal error code

    def run(self):
        if self.can_only_run_instruction_once:
            if self.pointer in self.run_history:
                return True
            self.run_history.append(self.pointer)

        instruction_split = self.instructions[self.pointer].split(" ")
        instruction = instruction_split[0]
        instruction_value = int(instruction_split[1])

        # execute instruction
        if instruction == "acc":
            self.accumulator += instruction_value
        elif instruction == "jmp":
            self.pointer += instruction_value
            return

        # increase pointer
        self.pointer += 1
