# https://adventofcode.com/2022/day/7
# --- Day 7: No Space Left On Device ---

with open('day07/input.txt', 'r') as f:
    lines = [line.strip('\n') for line in f.readlines()]


class Item:
    """A file or directory."""

    def __init__(self, name: str, *, parent: "Directory | None" = None) -> None:
        self.name = name
        self.parent = parent

    def __repr__(self) -> str:
        return f'Item({self.name})'

    @property
    def size(self) -> int:
        return 0

    @property
    def uri(self) -> str:
        uri_string = self.name
        if self.parent:
            uri_string = f'{self.parent.uri}/{uri_string}'
        return uri_string

    def with_parent(self, parent: "Directory | None" = None):
        self.parent = parent
        return self

    def get_root_directory(self) -> "Directory | None":
        if isinstance(self.parent, Directory):
            return self.parent.get_root_directory()
        if isinstance(self, Directory):
            return self
        return None


class Directory(Item):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._items: list[Item] = []

    def __repr__(self) -> str:
        items_repr = ', '.join(repr(item) for item in self._items)
        return f'Dir({self.name}, items=[{items_repr}])'

    @property
    def items(self) -> list[Item]:
        return self._items

    @property
    def size(self) -> int:
        total_size = 0
        for item in self._items:
            total_size += item.size
        return total_size

    def find_item(self, name: str, deep: bool = False) -> Item | None:
        for item in self._items:
            if item.name == name:
                return item
            if deep and isinstance(item, Directory):
                return item.find_item(name, deep=True)
        return None

    def contains_item(self, name: str, deep: bool = False):
        return self.find_item(name=name, deep=deep) is not None

    def create_directory(self, name: str):
        for item in self._items:
            if item.name == name:
                # Do nothing if the directory already exists.
                if isinstance(item, Directory):
                    return item
                raise ValueError(
                    'Cannot create directory, file already exists with name: ' + name)
        new_directory = Directory(name).with_parent(self)
        self._items.append(new_directory)
        return new_directory

    def create_file(self, name: str, size: int):
        for item in self._items:
            if item.name == name:
                # Do nothing if the file already exists.
                if isinstance(item, File):
                    return item
                raise ValueError(
                    'Cannot create file, directory already exists with name: ' + name)
        new_file = File(name, size).with_parent(self)
        self._items.append(new_file)
        return new_file

    def get_file_tree_lines(self, level: int = 0):
        indent = '  ' * level
        file_tree: list[str] = []
        file_tree.append(indent + f'- {self.name} (dir)')
        for item in self.items:
            if isinstance(item, Directory):
                file_tree += item.get_file_tree_lines(level=level + 1)
            else:
                file_tree.append(
                    indent + f'- {item.name} (file, size={item.size})')
        return file_tree

    def print_file_tree(self, level: int = 0):
        print('\n'.join(self.get_file_tree_lines(level=level)))


class File(Item):
    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self._size = size

    def __repr__(self) -> str:
        return f'File({self.name}, size={self.size})'

    @property
    def size(self) -> int:
        return self._size


# First, build the entire file system.
root_directory = Directory('/.')
# Assume that the first line is always '$ cd /'.
current_directory: Directory = root_directory
for i, line in enumerate(lines[1:]):
    # print(f'- Read line {i + 2}: {line}')
    if line == '$ ls':
        pass
    elif line == '$ cd ..':
        if not current_directory.parent:
            raise AssertionError('Cannot go to parent of root directory')
        current_directory = current_directory.parent
    elif line.startswith('$ cd'):
        next_directory_name = line.split('$ cd ')[1]
        next_directory = current_directory.find_item(
            next_directory_name, deep=False)
        if isinstance(next_directory, Directory):
            current_directory = next_directory
        else:
            raise AssertionError(
                f'cd command argument invalid: {next_directory}')
    elif line.startswith('dir '):
        new_directory_name = line.split('dir ')[1]
        current_directory.create_directory(new_directory_name)
    # Must be a file (1000 file.txt).
    else:
        file_size = int(line.split(' ')[0])
        file_name = line.split(' ')[1]
        current_directory.create_file(file_name, file_size)

# print(current_directory.uri)
# root_directory.print_file_tree()


def get_sum_directory_size_recursive(dir: Directory, max_size: int) -> int:
    sum_directory_size = 0
    if (current_directory_size := dir.size) <= max_size:
        sum_directory_size += current_directory_size

    for item in dir.items:
        if isinstance(item, Directory):
            sum_directory_size += get_sum_directory_size_recursive(
                item, max_size=max_size)
    return sum_directory_size


# Next, check every directory size.
sum_directory_sizes_max_100_000 = get_sum_directory_size_recursive(
    root_directory, 100_000)
print(f'{sum_directory_sizes_max_100_000 = }')  # 1543140


# ---------------------------------------------------------
# --- Part Two ---
# ---------------------------------------------------------

FILE_SYSTEM_SIZE = 70_000_000
REQUIRED_SPACE = 30_000_000
root_directory_size = root_directory.size
min_delete_size = REQUIRED_SPACE + root_directory_size - FILE_SYSTEM_SIZE
# print(f'{min_delete_size = }')
assert min_delete_size > 0


def get_smallest_directory_to_delete_size(dir: Directory, min_size: int) -> int:
    # Child directories must be less than min size if current dir is less than
    # min size.
    if (current_directory_size := dir.size) < min_size:
        return 0
    delete_directory_size = current_directory_size

    for item in dir.items:
        if isinstance(item, Directory):
            child_directory_size = get_smallest_directory_to_delete_size(
                item, min_size=min_size)
            if 0 < child_directory_size < delete_directory_size:
                delete_directory_size = child_directory_size
    return delete_directory_size


directory_to_delete_size = get_smallest_directory_to_delete_size(
    root_directory, min_delete_size)
print(f'{directory_to_delete_size = }')  # 1117448
