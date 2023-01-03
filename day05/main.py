# https://adventofcode.com/2022/day/5
# --- Day 5: Supply Stacks ---

import copy


with open('day05/input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]


def init_stacks(stack_count: int):
    stacks: list[list[str]] = []
    for _ in range(stack_count):
        stacks.append([])
    return stacks


# First, parse data.
STACK_COUNT = 9

# Save initial arrangement for part 2
stacks_initial = init_stacks(STACK_COUNT)
section_split_index = lines.index('')

# Parse initial crates.
for line in lines[:section_split_index - 1][::-1]:
    for stack_number in range(0, STACK_COUNT):
        crate = line[stack_number * 4 + 1]
        if crate != ' ':
            stacks_initial[stack_number].append(crate)

stacks = copy.deepcopy(stacks_initial)
# print(stacks)

# Execute procedure.
for line in lines[section_split_index + 1:]:
    move_amount = int(line.split('move')[1].split('from')[0].strip())
    start = int(line.split('from')[1].split('to')[0].strip())
    end = int(line.split('to')[1].strip())
    # print(f'{move_amount} : {start} : {end}')
    for _ in range(move_amount):
        stacks[end - 1].append(stacks[start - 1].pop())
# print(stacks)

stack_top = ''
for stack in stacks:
    stack_top += stack[-1]

print(f'{stack_top = }')  # ZWHVFWQWW


# --- Part Two ---

stacks2 = copy.deepcopy(stacks_initial)

for line in lines[section_split_index + 1:]:
    move_amount = int(line.split('move')[1].split('from')[0].strip())
    start = int(line.split('from')[1].split('to')[0].strip())
    end = int(line.split('to')[1].strip())
    # Pop to temp stack to return crate order.
    temp_stack = []
    for _ in range(move_amount):
        temp_stack.append(stacks2[start - 1].pop())
    for _ in range(len(temp_stack)):
        stacks2[end - 1].append(temp_stack.pop())
# print(stacks2)

stack_top_2 = ''
for stack in stacks2:
    stack_top_2 += stack[-1]

print(f'{stack_top_2 = }')  # HZFZCCWWV
