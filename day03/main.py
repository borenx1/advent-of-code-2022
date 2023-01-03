# https://adventofcode.com/2022/day/3
# --- Day 3: Rucksack Reorganization ---

import re


with open('day03/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def get_common_item_type(a: str, b: str) -> str:
    a_set = set(a)
    b_set = set(b)
    common = a_set.intersection(b_set)
    if len(common) != 1:
        raise ValueError('Invalid common item type: ' + common)
    return common.pop()


def get_item_type_priority(letter: str):
    if re.fullmatch(r'[a-z]', letter):
        return ord(letter) - 96
    if re.fullmatch(r'[A-Z]', letter):
        return ord(letter) - 38
    raise ValueError('Invalid item type: ' + letter)


priority_sum = 0

for line in lines:
    size = len(line)
    comp_a = line[:int(size/2)]
    comp_b = line[int(size/2):]
    common_item_type = get_common_item_type(comp_a, comp_b)
    # print(f'{comp_a}:{comp_b}')
    # print(common_item_type)
    priority_sum += get_item_type_priority(common_item_type)  # 7967

print(f'{priority_sum = }')


# --- Part Two ---

def get_common_badge(elf1: str, elf2: str, elf3: str) -> str:
    elf1_set = set(elf1)
    elf2_set = set(elf2)
    elf3_set = set(elf3)
    common = elf1_set.intersection(elf2_set).intersection(elf3_set)
    if len(common) != 1:
        raise ValueError('Invalid common badge: ' + common)
    return common.pop()


priority_sum_2 = 0
group_number = 0

for i in range(int(len(lines)/3)):
    elf1 = lines[i*3]
    elf2 = lines[i*3 + 1]
    elf3 = lines[i*3 + 2]
    common_badge = get_common_badge(elf1, elf2, elf3)
    # print(f'{comp_a}:{comp_b}')
    # print(common_item_type)
    priority_sum_2 += get_item_type_priority(common_badge)  # 2716

print(f'{priority_sum_2 = }')
