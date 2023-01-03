# https://adventofcode.com/2022/day/1
# --- Day 1: Calorie Counting ---

from collections import defaultdict


# Mapping of elf no. to total calories.
elves = defaultdict(lambda: 0)

with open('day01/input.txt', 'r') as f:
    lines = f.readlines()

elf_count = 0
for line in lines:
    line = line.strip()
    if line:
        elves[elf_count] += int(line)
    else:
        elf_count += 1

# print(elves)

most_calories = max(elves.values())

print(f'{most_calories = }')  # 72718


# --- Part Two ---

calories_list = list(elves.values())
top_three_calories = 0
for i in range(3):
    top_cal = max(calories_list)
    top_three_calories += top_cal
    calories_list.remove(top_cal)

print(f'{top_three_calories = }')  # 213089
