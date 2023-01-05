# https://adventofcode.com/2022/day/8
# --- Day 8: Treetop Tree House ---

with open('day08/input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]


def get_grid() -> list[list[int]]:
    grid = []
    for line in lines:
        row = []
        for height in line:
            row.append(int(height))
        grid.append(row)
    return grid


def is_tree_visible_from_top(grid: list[list[int]], row: int, col: int):
    tree_height = grid[row][col]
    for i in range(row):
        if grid[i][col] >= tree_height:
            return False
    return True


def is_tree_visible_from_bottom(grid: list[list[int]], row: int, col: int):
    tree_height = grid[row][col]
    for i in range(len(grid) - 1, row, -1):
        if grid[i][col] >= tree_height:
            return False
    return True


def is_tree_visible_from_left(grid: list[list[int]], row: int, col: int):
    tree_height = grid[row][col]
    for i in range(col):
        if grid[row][i] >= tree_height:
            return False
    return True


def is_tree_visible_from_right(grid: list[list[int]], row: int, col: int):
    tree_height = grid[row][col]
    for i in range(len(grid[0]) - 1, col, -1):
        if grid[row][i] >= tree_height:
            return False
    return True


def is_tree_visible(grid: list[list[int]], row: int, col: int):
    row_size = len(grid)
    col_size = len(grid[0])
    if row <= 0 or row >= row_size - 1 or col <= 0 or col >= col_size - 1:
        return True
    if is_tree_visible_from_top(grid, row, col):
        return True
    if is_tree_visible_from_left(grid, row, col):
        return True
    if is_tree_visible_from_bottom(grid, row, col):
        return True
    if is_tree_visible_from_right(grid, row, col):
        return True
    return False


grid = get_grid()
num_visible_trees = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if is_tree_visible(grid, i, j):
            num_visible_trees += 1

print(f'{num_visible_trees = }')  # 1717


# ---------------------------------------------------------
# --- Part Two ---
# ---------------------------------------------------------

def num_trees_visible_on_top(grid: list[list[int]], row: int, col: int):
    trees_visible = 0
    tree_height = grid[row][col]
    for i in range(row - 1, -1, -1):
        trees_visible += 1
        if grid[i][col] >= tree_height:
            return trees_visible
    return trees_visible


def num_trees_visible_on_bottom(grid: list[list[int]], row: int, col: int):
    trees_visible = 0
    tree_height = grid[row][col]
    for i in range(row + 1, len(grid)):
        trees_visible += 1
        if grid[i][col] >= tree_height:
            return trees_visible
    return trees_visible


def num_trees_visible_on_left(grid: list[list[int]], row: int, col: int):
    trees_visible = 0
    tree_height = grid[row][col]
    for i in range(col - 1, -1, -1):
        trees_visible += 1
        if grid[row][i] >= tree_height:
            return trees_visible
    return trees_visible


def num_trees_visible_on_right(grid: list[list[int]], row: int, col: int):
    trees_visible = 0
    tree_height = grid[row][col]
    for i in range(col + 1, len(grid[0])):
        trees_visible += 1
        if grid[row][i] >= tree_height:
            return trees_visible
    return trees_visible


highest_score = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        num_visible_top = num_trees_visible_on_top(grid, i, j)
        num_visible_bottom = num_trees_visible_on_bottom(grid, i, j)
        num_visible_left = num_trees_visible_on_left(grid, i, j)
        num_visible_right = num_trees_visible_on_right(grid, i, j)
        score = num_visible_top * num_visible_bottom * \
            num_visible_left * num_visible_right
        if score > highest_score:
            highest_score = score

print(f'{highest_score = }')  # 321975
