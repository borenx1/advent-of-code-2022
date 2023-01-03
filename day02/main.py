# https://adventofcode.com/2022/day/2
# --- Day 2: Rock Paper Scissors ---


# A/X = rock, B/Y = paper, C/Z = scissors.

def get_score(opponent: str, own: str) -> int:
    score = 0

    if own == 'X':  # rock
        score += 1
    elif own == 'Y':  # paper
        score += 2
    elif own == 'Z':  # scissors
        score += 3
    else:
        raise ValueError('Invalid own shape: ' + own)

    if opponent == 'A':  # rock
        if own == 'X':  # rock
            score += 3
        elif own == 'Y':
            score += 6  # paper
        else:  # scissors
            pass
    elif opponent == 'B':  # paper
        if own == 'X':  # rock
            pass
        elif own == 'Y':  # paper
            score += 3
        else:  # scissors
            score += 6
    elif opponent == 'C':  # scissors
        if own == 'X':  # rock
            score += 6
        elif own == 'Y':  # paper
            pass
        else:  # scissors
            score += 3
    else:
        raise ValueError('Invalid opponent shape: ' + opponent)
    return score


with open('day02/input.txt', 'r') as f:
    lines = f.readlines()

total_score = 0
for line in lines:
    opponent, own = line.strip().split(' ')
    # print(f'{opponent}: {own}')
    total_score += get_score(opponent, own)

print(f'{total_score = }')  # 14531


# --- Part Two ---

def get_score_2(opponent: str, result: str) -> int:
    score = 0

    if result == 'X':  # LOSE
        if opponent == 'A':  # rock
            score += 3  # scissors
        elif opponent == 'B':  # paper
            score += 1  # rock
        else:  # scissors
            score += 2  # paper
    elif result == 'Y':  # DRAW
        score += 3
        if opponent == 'A':  # rock
            score += 1  # rock
        elif opponent == 'B':  # paper
            score += 2  # paper
        else:  # scissors
            score += 3  # scissors
    elif result == 'Z':  # WIN
        score += 6
        if opponent == 'A':  # rock
            score += 2  # paper
        elif opponent == 'B':  # paper
            score += 3  # scissors
        else:  # scissors
            score += 1  # rock
    else:
        raise ValueError('Invalid result: ' + result)
    return score


total_score_2 = 0
for line in lines:
    opponent, result = line.strip().split(' ')
    total_score_2 += get_score_2(opponent, result)

print(f'{total_score_2 = }')  # 11258
