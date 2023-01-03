# https://adventofcode.com/2022/day/4
# --- Day 4: Camp Cleanup ---

with open('day04/input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]


def get_section_set(section_range: str):
    nums = section_range.split('-')
    section_min = int(nums[0])
    section_max = int(nums[1])
    return set(range(section_min, section_max + 1))


fully_contained_count = 0

for line in lines:
    section_ranges = line.split(',')
    section_range_1 = get_section_set(section_ranges[0])
    section_range_2 = get_section_set(section_ranges[1])
    if section_range_1.issubset(section_range_2) or section_range_1.issuperset(section_range_2):
        fully_contained_count += 1

print(f'{fully_contained_count = }')  # 513


# --- Part Two ---

overlapped_count = 0

for line in lines:
    section_ranges = line.split(',')
    section_range_1 = get_section_set(section_ranges[0])
    section_range_2 = get_section_set(section_ranges[1])
    if section_range_1.intersection(section_range_2):
        overlapped_count += 1

print(f'{overlapped_count = }')  # 878
