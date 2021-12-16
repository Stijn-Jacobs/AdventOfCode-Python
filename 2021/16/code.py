# Advent of code Year 2021 Day 16 solution
# Author = Stijn-Jacobs
# Date = December 2021
from math import floor

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readline()


class Packet:
    def __init__(self, decode_from):
        self.version = None
        self.type_id = None
        self.value = None
        self.sub_packets = []
        self.length = self.decode_from(decode_from)

    def decode_from(self, inp):
        print("from: " + str(inp))
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
                    self.value = int(literal_value_binary, 2)
                    return 6 + (group * 5) + 5
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
                return 6 + length_sum + 1 + 15
            else:
                # Next 11 bits indicate the amount of subpackets
                amount = int(inp[0:11], 2)
                inp = inp[11:]
                index = 0
                for i in range(0, amount):
                    packet = Packet(inp[index:])
                    self.sub_packets.append(packet)
                    index += packet.packet_length()
                return 6 + index + 1 + 11

    def packet_length(self):
        return self.length

    def __repr__(self):
        return "V: " + str(self.version) + ", Type: " + str(self.type_id) + " Value: " + str(self.value) + ", " + str(
            [str(pack) for pack in self.sub_packets])

    def version_sum(self):
        version_sum = 0
        for packet in self.sub_packets:
            version_sum += packet.version_sum()
        return version_sum + self.version


def binary_representation(inp):
    arr = ""
    for char in inp:
        arr += bin(int(char, 16))[2:].zfill(4)
    return arr


root_packet = Packet(binary_representation(input))
for packet in root_packet.sub_packets:
    print(packet)
print("Part One : " + str(root_packet.version_sum()))

print("Part Two : " + str(None))
