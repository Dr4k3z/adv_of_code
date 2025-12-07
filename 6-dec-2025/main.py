import sys

sys.path.append("..")

from utils import read_input

maths = {
    "+": lambda x, y: x + y,
    "*": lambda x, y: x * y,
}


def transpose(matrix: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in zip(*matrix, strict=False)]


def part1() -> None:
    data = read_input("input.txt")

    problems = []
    for line in data[:-1]:
        if type(line) is not str:
            continue

        elements = line.split()
        problems.append([int(el) for el in elements])

    problems = transpose(problems)

    if type(data[-1]) is not str:
        raise ValueError("Last line must be a string of operations")
    operations = [maths[el] for el in data[-1].split()]

    total = 0
    for p, o in zip(problems, operations, strict=False):
        result = p[0]
        for i in range(1, len(p)):
            result = o(result, p[i])  # type: ignore
        total += result

    print(total)


def parse_cephalopod(lines: list[str]) -> list[list[int]]:
    if not lines:
        return []

    height = len(lines)
    width = max(len(line) for line in lines)

    grid = [line.ljust(width) for line in lines]

    problems: list[list[int]] = []

    col = 0
    while col < width:
        if all(grid[row][col] == " " for row in range(height)):
            col += 1
            continue

        group_cols: list[int] = []
        while col < width and not all(grid[row][col] == " " for row in range(height)):
            group_cols.append(col)
            col += 1

        column_numbers: list[int] = []
        for c in group_cols:
            digits = [
                grid[row][c]
                for row in range(height - 1)  # exclude bottom row (operators)
                if grid[row][c] != " "
            ]
            column_numbers.append(int("".join(digits)))

        problems.append(list(reversed(column_numbers)))

    problems.reverse()
    return problems


def read_raw(filename: str = "input.txt") -> list[str]:
    with open(filename) as f:
        return [line.rstrip("\n") for line in f]


def part2() -> None:
    data = read_raw("input.txt")
    problems = parse_cephalopod(data)

    if type(data[-1]) is not str:
        raise ValueError("Last line must be a string of operations")
    operations = [el for el in data[-1].split()][::-1]

    total = 0
    for p, o in zip(problems, operations, strict=False):
        result = p[0]
        for i in range(1, len(p)):
            result = maths[o](result, p[i])  # type: ignore
        total += result

    print(total)


if __name__ == "__main__":
    # part1()
    part2()
