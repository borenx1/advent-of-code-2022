# https://adventofcode.com/2022/day/11
# --- Day 11: Monkey in the Middle ---

from typing import Callable


with open('day11/input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]


class Monkey:
    def __init__(
        self,
        operation: Callable[[int], int],
        test: Callable[[int], bool],
        true_throw_to: int,
        false_throw_to: int,
        items: list[int] | None = None
    ) -> None:
        self.operation = operation
        self.test = test
        self.true_throw_to = true_throw_to
        self.false_throw_to = false_throw_to
        self.items = []
        if items:
            self.items = items.copy()

    def __repr__(self) -> str:
        return f'Monkey({repr(self.items)})'


def init_monkeys(input_lines: list[str]) -> list[Monkey]:
    monkeys: list[Monkey] = []
    monkey_count = 0
    starting_items: list[int] = []
    operation: Callable[[int], int] = lambda x: x
    test: Callable[[int], bool] = lambda x: True
    true_throw_to = 0  # Money to throw to on True condition
    false_throw_to = 0  # Money to throw to on False condition

    for line in input_lines:
        if line.startswith('Monkey'):
            assert int(line[6:-1]) == monkey_count
        elif line.strip().startswith('Starting'):
            starting_items = [int(x) for x in line.split(':')[1].split(',')]
        elif line.strip().startswith('Operation'):
            equation_rhs = line.split('=')[1].strip()
            # Assume limited types of equations.
            if equation_rhs == 'old * old':
                def operation(x): return x * x
            elif 'old *' in equation_rhs:
                # Have to use function to create operation to lose reference to
                # "line" variable.
                def generate_operation(operand):
                    return lambda x: x * operand
                operation = generate_operation(int(equation_rhs.split('*')[1]))
            elif 'old +' in equation_rhs:
                def generate_operation(operand):
                    return lambda x: x + operand
                operation = generate_operation(int(equation_rhs.split('+')[1]))
            else:
                raise AssertionError(f'Unrecognized equation type: {line}')
        elif line.strip().startswith('Test'):
            def generate_test(divisor):
                return lambda x: x % divisor == 0
            test = generate_test(int(line.split('by')[1]))
        elif line.strip().startswith('If true'):
            true_throw_to = int(line.split('monkey')[1])
        elif line.strip().startswith('If false'):
            false_throw_to = int(line.split('monkey')[1])
            # Create monkey at last line for each monkey.
            monkeys.append(Monkey(
                operation=operation,
                test=test,
                true_throw_to=true_throw_to,
                false_throw_to=false_throw_to,
                items=starting_items
            ))
        elif line == "":
            monkey_count += 1
        else:
            raise AssertionError(f'Unrecognized line: {line}')
    return monkeys


def execute_round(monkeys: list[Monkey]) -> list[int]:
    inspect_counts: list[int] = []
    for monkey in monkeys:
        inspect_count = 0
        for item in monkey.items:
            # First, inspect (apply operation).
            item = monkey.operation(item)
            inspect_count += 1
            # Second, decrease worry level.
            item = item // 3
            # Third, test worry level.
            test_result = monkey.test(item)
            # Finally, throw to monkey depending on test.
            if test_result:
                # Assume monkey count starts at 0.
                monkeys[monkey.true_throw_to].items.append(item)
            else:
                monkeys[monkey.false_throw_to].items.append(item)
        monkey.items = []  # The monkey throws all the items it has.
        inspect_counts.append(inspect_count)
    return inspect_counts


def get_max_two_numbers(numbers: list[int]):
    assert len(numbers) >= 2
    numbers_copy = numbers.copy()
    max_num_1 = max(numbers_copy)
    numbers_copy.pop(numbers_copy.index(max_num_1))
    max_num_2 = max(numbers_copy)
    return max_num_1, max_num_2


monkeys = init_monkeys(lines)
total_inspect_counts = [0 for _ in range(len(monkeys))]
# Run rounds and sum up inspect counts.
for _ in range(20):
    inspect_counts = execute_round(monkeys)
    for i in range(len(total_inspect_counts)):
        total_inspect_counts[i] += inspect_counts[i]

# for i in range(len(monkeys)):
#     print(f'Monkey {i} inspected items {total_inspect_counts[i]} times.')

# Get product of max 2 inspect counts (monkey business).
max_inspect_count_1, max_inspect_count_2 = get_max_two_numbers(
    total_inspect_counts)
monkey_business = max_inspect_count_1 * max_inspect_count_2

print(f'{monkey_business = }')  # 56595


# ---------------------------------------------------------
# --- Part Two ---
# ---------------------------------------------------------

def execute_round_2(monkeys: list[Monkey]) -> list[int]:
    inspect_counts: list[int] = []
    for monkey in monkeys:
        inspect_count = 0
        for item in monkey.items:
            # First, inspect (apply operation).
            item = monkey.operation(item)
            inspect_count += 1
            # Second, test worry level (no longer decreased).
            test_result = monkey.test(item)
            # Third, manage worry level or else it will grow exponentially,
            # this will make the script take too long to run.
            # Note: The test divisor is a prime number.
            # After trial and error, I found out that getting the remainder
            # of the item worry level divided by the product of the prime
            # numbers used as divisors in the input will produce the same
            # results (test simulated over many rounds).
            item = item % (2*3*5*7*11*13*17*19)
            # Finally, throw to monkey depending on test.
            if test_result:
                # Assume monkey count starts at 0.
                monkeys[monkey.true_throw_to].items.append(item)
            else:
                monkeys[monkey.false_throw_to].items.append(item)
        monkey.items = []  # The monkey throws all the items it has.
        inspect_counts.append(inspect_count)
    return inspect_counts


monkeys_2 = init_monkeys(lines)
total_inspect_counts_2 = [0 for _ in range(len(monkeys_2))]
# Run rounds and sum up inspect counts.
for _ in range(10000):
    inspect_counts = execute_round_2(monkeys_2)
    for i in range(len(total_inspect_counts_2)):
        total_inspect_counts_2[i] += inspect_counts[i]

# for i in range(len(monkeys_2)):
#     print(f'Monkey {i} inspected items {total_inspect_counts_2[i]} times.')

max_inspect_count_1, max_inspect_count_2 = get_max_two_numbers(
    total_inspect_counts_2)
monkey_business_2 = max_inspect_count_1 * max_inspect_count_2

print(f'{monkey_business_2 = }')  # 15693274740
