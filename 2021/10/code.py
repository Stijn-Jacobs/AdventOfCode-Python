# Advent of code Year 2021 Day 10 solution
# Author = Stijn-Jacobs
# Date = December 2021

with open((__file__.rstrip("code.py") + "input.txt"), 'r') as input_file:
    input = input_file.readlines()

corrupted_syntax_points_map = {')': 3,
                               ']': 57,
                               '}': 1197,
                               '>': 25137}

incomplete_syntax_points_map = {')': 1,
                                ']': 2,
                                '}': 3,
                                '>': 4}

matching_chunk_char = {'(': ')',
                       '[': ']',
                       '{': '}',
                       '<': '>'}


def increase_remaining_tag(dict, add_to):
    dict[add_to] = dict.get(add_to, 0) + 1
    return dict


# Returns a tuple containing True if corrupted with a score and False if incomplete with its score
def check_line_score(inp):
    opened = []
    for char in inp.strip():
        # Opening of another chunk
        if char in matching_chunk_char.keys():
            opened.append(char)
        else:
            start_char = opened.pop()
            if matching_chunk_char[start_char] != char:
                # Corrupted line
                return True, corrupted_syntax_points_map[char]
    # Line is incomplete, autocomplete the rest and calc score
    incomplete_score = 0
    opened.reverse()
    for item in opened:
        incomplete_score *= 5
        incomplete_score += incomplete_syntax_points_map[matching_chunk_char[item]]

    return False, incomplete_score


# Returns the scores, corrupted first, incomplete second
def find_scores(inp):
    corrupted_score = 0
    incomplete_score_arr = []
    for line in inp:
        score = check_line_score(line)
        if score[0]:
            corrupted_score += score[1]
        else:
            incomplete_score_arr.append(score[1])

    incomplete_score_arr.sort()
    return corrupted_score, incomplete_score_arr[int(len(incomplete_score_arr) / 2)]


scores = find_scores(input)

print("Part One : " + str(scores[0]))

print("Part Two : " + str(scores[1]))
