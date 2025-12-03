import sys

sys.path.append("..")

from utils import read_input


def part1() -> None:
    input = read_input("input.txt")

    s = 0
    for line in input:
        bank = [int(x) for x in line]

        first = max(bank[:-1])
        idx = bank.index(first)
        second = max(bank[idx + 1 :])

        s += (first * 10) + second

    print(s)


def best_12_digits(line: str) -> int:
    digits = line.strip()
    keep = 12
    to_remove = len(digits) - keep

    stack: list[str] = []

    for d in digits:
        while to_remove > 0 and stack and stack[-1] < d:
            stack.pop()
            to_remove -= 1
        stack.append(d)

    if to_remove > 0:
        stack = stack[:-to_remove]

    chosen = "".join(stack[:keep])
    return int(chosen)


def part2() -> None:
    input = read_input("input.txt")

    s = 0
    for line in input:
        if type(line) is not str:
            raise ValueError("Expected string input")

        s += best_12_digits(line)

    print(s)


if __name__ == "__main__":
    # part1()
    part2()
