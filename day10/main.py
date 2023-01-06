# https://adventofcode.com/2022/day/10
# --- Day 10: Cathode-Ray Tube ---

with open('day10/input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]


def noop(cycle: int, register: int) -> tuple[int, int]:
    return (cycle + 1, register)


def addx_one(cycle: int, register: int, value: int) -> tuple[int, int]:
    return (cycle + 1, register)


def addx_two(cycle: int, register: int, value: int) -> tuple[int, int]:
    return (cycle + 1, register + value)


def signal_strength(cycle: int, register: int):
    return cycle * register


def count_signal_strength(init: int, cycle: int, register: int, checkpoints: list[int]):
    if cycle in checkpoints:
        return init + signal_strength(cycle, register)
    return init


cycle = 1  # Count during the cycle (start at 1)
register_x = 1
cycle_checkpoints = [20, 60, 100, 140, 180, 220]
signal_strength_sum = 0

for line in lines:
    command = line[:4]
    if command == 'noop':
        cycle, register_x = noop(cycle, register_x)
    elif command == 'addx':
        value = int(line[5:])
        cycle, register_x = addx_one(cycle, register_x, value)
        signal_strength_sum = count_signal_strength(signal_strength_sum, cycle,
                                                    register_x, cycle_checkpoints)
        cycle, register_x = addx_two(cycle, register_x, value)
    else:
        raise ValueError('Invalid command: ' + command)
    signal_strength_sum = count_signal_strength(signal_strength_sum, cycle,
                                                register_x, cycle_checkpoints)
    # print(f'{cycle = }, X = {register_x}')

print(f'{signal_strength_sum = }')  # 14160


# ---------------------------------------------------------
# --- Part Two ---
# ---------------------------------------------------------

ROWS = 6
COLS = 40


def draw_crt(crt: str, cycle: int, lit: bool):
    crt += '#' if lit else '.'
    if cycle % COLS == 0:
        crt += '\n'
    return crt


def is_pixel_lit(cycle: int, register: int) -> bool:
    pixel_pos = cycle - 1
    pixel_col = pixel_pos % COLS
    sprite_col = register
    # print(f'{cycle = }, {pixel_col = }, {sprite_col = }')
    return abs(pixel_col - sprite_col) <= 1


cycle = 1
register_x = 1
CRT = ''

for line in lines:
    CRT = draw_crt(CRT, cycle, is_pixel_lit(cycle, register_x))
    command = line[:4]
    if command == 'noop':
        cycle, register_x = noop(cycle, register_x)
    elif command == 'addx':
        value = int(line[5:])
        cycle, register_x = addx_one(cycle, register_x, value)
        CRT = draw_crt(CRT, cycle, is_pixel_lit(cycle, register_x))
        cycle, register_x = addx_two(cycle, register_x, value)
    else:
        raise ValueError('Invalid command: ' + command)
    # print(f'{cycle = }, X = {register_x}')

print(CRT)  # RJERPEFC
