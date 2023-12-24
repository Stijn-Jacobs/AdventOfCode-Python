# Advent of code Year 2023 Day 7 solution
# Author = Stijn-Jacobs
# Date = December 2023

import numpy as np

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

jokers_enabled = False


class Card:
    def __init__(self, value):
        self.value = value

    # card values with the highest being left, A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    def get_card_value(self):
        if self.value == "A":
            return 14
        elif self.value == "K":
            return 13
        elif self.value == "Q":
            return 12
        elif self.value == "J":
            if jokers_enabled:
                return 1
            else:
                return 11
        elif self.value == "T":
            return 10
        else:
            return int(self.value)

    def __lt__(self, other):
        return self.get_card_value() < other.get_card_value()


class Hand:

    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    # return the type of hand
    def hand_type(self):
        # create map how often a card occurs
        card_map = {}
        for card in self.cards:
            if card.value in card_map:
                card_map[card.value] += 1
            else:
                card_map[card.value] = 1

        # sort the map
        card_map = dict(sorted(card_map.items(), key=lambda item: item[1], reverse=True))

        # if joker is present, add the amount of jokers to the top card, and remove original 'J'.
        # also check if jokers are enabled, and if not all the values in the hand are jokers.
        if jokers_enabled and "J" in card_map and card_map["J"] != 5:
            # get the top most card that isn't a joker
            index = 0

            while list(card_map.keys())[index] == "J":
                index += 1

            card_map[list(card_map.keys())[index]] += card_map["J"]
            del card_map["J"]

        # check for five of a kind
        if len(card_map) == 1:
            return 6
        # check for four of a kind
        elif len(card_map) == 2 and list(card_map.values())[0] == 4:
            return 5
        # check for full house
        elif len(card_map) == 2 and list(card_map.values())[0] == 3:
            return 4
        # check for three of a kind
        elif len(card_map) == 3 and list(card_map.values())[0] == 3:
            return 3
        # check for two pair
        elif len(card_map) == 3 and list(card_map.values())[0] == 2:
            return 2
        # check for one pair
        elif len(card_map) == 4:
            return 1

        return 0

    # compare function, first compare based on hand type, then on value of the card
    def __lt__(self, other):
        o_hand_type = other.hand_type()
        hand_type = self.hand_type()
        if hand_type == o_hand_type:
            # compare based on value of the first card, if these are the same check the second card, etc.
            for i in range(len(self.cards)):
                if self.cards[i] < other.cards[i]:
                    return True
                elif self.cards[i] > other.cards[i]:
                    return False
        else:
            return hand_type < o_hand_type


hands = []

for hand in input:
    cards = []
    for card in hand.split(" ")[0]:
        cards.append(Card(card))
    hands.append(Hand(cards, int(hand.split(" ")[1])))


def play():
    # sort the hands
    hands.sort()

    sum = 0
    # print the hands in order
    i = 1
    for hand in hands:
        sum += hand.bid * i
        i += 1

    return sum


def part1():
    return play()


def part2():
    global jokers_enabled
    jokers_enabled = True

    return play()


print(part1())
print(part2())
