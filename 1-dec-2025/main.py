import sys

sys.path.append("..")

from utils import execution_time, read_input, save_output


def part1() -> None:
    data = read_input("input.txt")

    dial = 50
    counter = 0
    for line in data:
        direction, value = line[:1], line[1:]

        if type(value) is not str:
            raise ValueError("Value should be a string")

        if direction == "L":
            dial -= int(value)
            dial %= 99 + 1
        elif direction == "R":
            dial += int(value)
            dial %= 99 + 1
        else:
            raise ValueError(f"Unknown direction: {direction}")

        if dial == 0:
            counter += 1

    print(f"Reached zero {counter} times.")


def part2() -> None:
    data = read_input("input.txt")

    dial = 50
    hits_zero = 0

    for line in data:
        direction, value_str = line[0], line[1:]
        if type(value_str) is not str:
            raise ValueError("Value should be a string")

        steps = int(value_str)
        sign = 1 if direction == "R" else -1

        if sign == 1:
            first_hit = (100 - dial) % 100
            if first_hit == 0:
                first_hit = 100
        else:
            first_hit = dial % 100
            if first_hit == 0:
                first_hit = 100

        if first_hit <= steps:
            hits_zero += 1 + (steps - first_hit) // 100

        dial = (dial + sign * steps) % 100

    print(f"Hit zero (while moving) {hits_zero} times.")


if __name__ == "__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    print(f"Part One execution time: {part1_time}")
    print(f"Part One execution time: {part2_time}")
    save_output(new_row=[part1_time, part2_time])
