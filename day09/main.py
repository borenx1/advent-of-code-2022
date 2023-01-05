# https://adventofcode.com/2022/day/9
# --- Day 9: Rope Bridge ---

with open('day09/input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'


def move(head: Coordinate, tail: Coordinate, direction: str, amount: int):
    # First move head
    def move_head_up():
        head.y += 1

    def move_head_down():
        head.y -= 1

    def move_head_left():
        head.x -= 1

    def move_head_right():
        head.x += 1
    if direction == 'U':
        move_head_func = move_head_up
    elif direction == 'D':
        move_head_func = move_head_down
    elif direction == 'L':
        move_head_func = move_head_left
    elif direction == 'R':
        move_head_func = move_head_right
    else:
        raise ValueError('Invalid direction: ' + direction)

    tail_positions = set([(tail.x, tail.y)])
    for _ in range(amount):
        move_head_func()
        # Then move tail
        if abs(head.x - tail.x) > 1:
            tail.x += 1 if (head.x > tail.x) else -1
            if head.y != tail.y:  # Move diagonally if not in line
                tail.y += 1 if (head.y > tail.y) else -1
        elif abs(head.y - tail.y) > 1:
            tail.y += 1 if (head.y > tail.y) else -1
            if head.x != tail.x:
                tail.x += 1 if (head.x > tail.x) else -1
        else:
            pass  # Tail does not move
        tail_positions.add((tail.x, tail.y))
    # Return all visited tail positions.
    return tail_positions


head = Coordinate(0, 0)
tail = Coordinate(0, 0)
tail_positions: set[tuple[int, int]] = set()

for line in lines:
    direction = line[0]
    amount = int(line[2:])
    tail_positions = tail_positions.union(move(head, tail, direction, amount))


# print(f'{head = }, {tail = }')
# print(tail_positions)
print(f'{len(tail_positions) = }')  # 6037

# print_grid = [['.'] * 400 for _ in range(400)]
# for pos in tail_positions:
#     print_grid[pos[1] + 200][pos[0] + 200] = '#'
# print('\n'.join(''.join(row) for row in print_grid))

# ---------------------------------------------------------
# --- Part Two ---
# ---------------------------------------------------------

# Slightly modify previous functions.


def move_head(head: Coordinate, direction: str):
    if direction == 'U':
        head.y += 1
    elif direction == 'D':
        head.y -= 1
    elif direction == 'L':
        head.x -= 1
    elif direction == 'R':
        head.x += 1
    else:
        raise ValueError('Invalid direction: ' + direction)


def move_tail(head: Coordinate, tail: Coordinate):
    if abs(head.x - tail.x) > 1:
        tail.x += 1 if (head.x > tail.x) else -1
        if head.y != tail.y:  # Move diagonally if not in line
            tail.y += 1 if (head.y > tail.y) else -1
    elif abs(head.y - tail.y) > 1:
        tail.y += 1 if (head.y > tail.y) else -1
        if head.x != tail.x:
            tail.x += 1 if (head.x > tail.x) else -1
    else:
        pass  # Tail does not move


def move_once(knots: list[Coordinate], direction: str):
    # First move head.
    move_head(knots[0], direction)
    # Then move tails in sequence.
    for i in range(len(knots) - 1):
        move_tail(knots[i], knots[i + 1])


def move_multiple(knots: list[Coordinate], direction: str, amount: int):
    tail = knots[-1]
    tail_positions = set([(tail.x, tail.y)])
    for _ in range(amount):
        move_once(knots, direction)
        tail = knots[-1]
        tail_positions.add((tail.x, tail.y))
    # Return all visited tail positions.
    return tail_positions


knots = [Coordinate(0, 0) for _ in range(10)]  # 10 knots
tail_positions_2: set[tuple[int, int]] = set()

for line in lines:
    direction = line[0]
    amount = int(line[2:])
    tail_positions_2 = tail_positions_2.union(
        move_multiple(knots, direction, amount))


# for i in range(len(knots)):
#     print(f'{knots[i] = }')
# print(tail_positions)
print(f'{len(tail_positions_2) = }')  # 2485
