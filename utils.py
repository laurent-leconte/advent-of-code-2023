from enum import IntEnum

class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    
    def __str__(self):
        return self.name

    def apply(self, x, y):
        if self == Direction.UP:
            return x, y - 1
        elif self == Direction.DOWN:
            return x, y + 1
        elif self == Direction.LEFT:
            return x - 1, y
        elif self == Direction.RIGHT:
            return x + 1, y
        
    def opposite(self):
        return Direction((self.value + 2) % 4)
    
    def perpendicular(self):
        if self in (Direction.UP, Direction.DOWN):
            return Direction.LEFT, Direction.RIGHT
        else:
            return Direction.UP, Direction.DOWN


def get_input(day: int, example=False, split_line=True) -> str:
    file = f"inputs/day{day}"
    if example:
        file += "_example"
    with open(file, "r") as f:
        content = f.read()
        if split_line:
            return content.splitlines()
        else:
            return content
        
def split_by_empty_line(input: list[str]) -> list[list[str]]:
    """
    Split a list of strings by empty lines, return a list of lists of strings
    """
    acc = []
    res = []
    for line in input:
        if line == '':
            res.append(acc)
            acc = []
        else:
            acc.append(line)
    if acc:
        res.append(acc)
    return res


def transpose(lines: list[str]):
    rows = [''] * len(lines[0])
    for line in lines:
        for i, c in enumerate(line):
            rows[i] += c
    return rows


def to_board(lines: list[str]) -> tuple[int, int, list[list[str]]]:
    """
    Convert a list of strings into a 2D array of characters
    """
    return len(lines[0]), len(lines), [list(line) for line in lines]


def to_int_board(lines: list[str]) -> tuple[int, int, list[list[int]]]:
    """
    Convert a list of strings into a 2D array of integers
    """
    return len(lines[0]), len(lines), [[int(c) for c in line] for line in lines]