# Advent of code Year 2020 Day 9 solution
# Author = Stijn-Jacobs
# Date = December 2020

from operator import itemgetter
from itertools import groupby


with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()


class Connection:
    preamble = 25

    def __init__(self, content):
        self.sums = []
        self.content = content

    def calculate_sums_at_index(self, index):
        sums = []
        last = self.content[index-self.preamble:index]
        for i in last:
            for j in last:
                sums.append(int(i) + int(j))
        return sums

    # get the first invalid value
    def get_first_invalid(self):
        content_no_preamble = self.content[self.preamble:]
        for index in range(0, len(content_no_preamble)):
            value = int(content_no_preamble[index].rstrip())
            if value not in self.calculate_sums_at_index(index + self.preamble):
                return value

    def contiguous_ints(self, target):
        cur_index = 0
        while cur_index < len(self.content):
            cur_sum = []
            content = self.content.copy()
            content.pop(cur_index)
            for index in range(cur_index, len(self.content)):
                sum_loop = sum(cur_sum)
                if sum_loop == target:
                    # found the values
                    cur_sum.sort()
                    return cur_sum[0], cur_sum[-1]
                if sum_loop > target:
                    break
                cur_sum.append(int(self.content[index].rstrip()))
            cur_index += 1


# part 1 code
con = Connection(input)
invalid_num = con.get_first_invalid()
print("Part One : " + str(invalid_num))

# part 2 code
part_2_answer = sum(con.contiguous_ints(invalid_num))
print("Part Two : " + str(part_2_answer))
