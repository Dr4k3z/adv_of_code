import sys

sys.path.append("..")

from utils import execution_time, read_input, save_output


def part1() -> None:
    input = read_input("input.txt")[0]
    if type(input) is not str:
        raise ValueError("Expected a single line of input.")

    s = 0
    for r in input.split(","):
        start, end = map(int, r.split("-"))

        for num in range(start, end + 1):
            num_str = str(num)
            n = len(num_str) // 2
            if num_str[:n] == num_str[n:]:
                s += num

    print(f"Sum of all invalid ids: {s}")


def check_sub(s: str, length: int) -> bool:
    if len(s) % length != 0:
        return False

    n = len(s) // length
    sub = s[:length]
    for i in range(1, n):
        if s[i * length : (i + 1) * length] != sub:
            return False
    return True


def part2() -> None:
    input = read_input("input.txt")[0]
    if type(input) is not str:
        raise ValueError("Expected a single line of input.")

    s = 0
    for r in input.split(","):
        start, end = map(int, r.split("-"))

        for num in range(start, end + 1):
            num_str = str(num)

            n = len(num_str)
            for i in range(1, n):
                if check_sub(num_str, i):
                    s += num
                    break

    print(f"Sum of all invalid ids: {s}")


if __name__ == "__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    print(f"Part One execution time: {part1_time}")
    print(f"Part One execution time: {part2_time}")

    save_output(new_row=[part1_time, part2_time])
