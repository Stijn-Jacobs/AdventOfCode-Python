# Advent of code Year 2021 Day 16 solution
# Author = Stijn-Jacobs
# Date = December 2021

import numpy as np
from math import floor

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readline()


class Packet:
    def __init__(self, decode_from):
        self.version = None
        self.type_id = None
        self._value = None
        self.sub_packets = []
        self.length = self.decode_from(decode_from)

    def decode_from(self, inp):
        self.version = int(inp[0:3], 2)
        self.type_id = int(inp[3:6], 2)
        inp = inp[6:]
        if self.type_id == 4:
            # Literal value
            literal_value_binary = ""
            for group in range(0, floor(len(inp) / 5)):
                val = inp[group * 5:(group * 5) + 5]
                literal_value_binary += val[1:]
                if int(val[0]) == 0:
                    # Last group of packet
                    self._value = int(literal_value_binary, 2)
                    return (group * 5) + 5
        else:
            # Ignore operators for now
            length_id = int(inp[0])
            inp = inp[1:]
            if length_id == 0:
                # Next 15 bits indicate the total length of sub-packets
                length = int(inp[:15], 2)
                inp = inp[15:]
                length_sum = 0
                while length_sum < length:
                    packet = Packet(inp[length_sum:])
                    self.sub_packets.append(packet)
                    length_sum += packet.packet_length()
                return length_sum + 1 + 15
            else:
                # Next 11 bits indicate the amount of sub-packets
                amount = int(inp[0:11], 2)
                inp = inp[11:]
                index = 0
                for i in range(0, amount):
                    packet = Packet(inp[index:])
                    self.sub_packets.append(packet)
                    index += packet.packet_length()
                return index + 1 + 11

    def packet_length(self):
        return self.length + 6

    def get_value(self):
        if self._value:
            return self._value
        sub_values = [sub.get_value() for sub in self.sub_packets]
        if self.type_id == 0:
            return sum(sub_values)
        elif self.type_id == 1:
            return sub_values[0] if len(sub_values) == 1 else np.prod(sub_values)
        elif self.type_id == 2:
            return min(sub_values)
        elif self.type_id == 3:
            return max(sub_values)
        elif self.type_id == 5:
            return 1 if sub_values[0] > sub_values[1] else 0
        elif self.type_id == 6:
            return 1 if sub_values[0] < sub_values[1] else 0
        elif self.type_id == 7:
            return 1 if sub_values[0] == sub_values[1] else 0
        return None

    def version_sum(self):
        version_sum = 0
        for packet in self.sub_packets:
            version_sum += packet.version_sum()
        return version_sum + self.version


def binary_representation(inp):
    return "".join([bin(int(char, 16))[2:].zfill(4) for char in inp])


root_packet = Packet(binary_representation(input))
print("Part One : " + str(root_packet.version_sum()))

print("Part Two : " + str(root_packet.get_value()))
