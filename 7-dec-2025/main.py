# type: ignore

import sys

sys.path.append("..")

from utils import execution_time, read_input, save_output


def part1() -> None:
    data = read_input("input.txt")

    counter = 0
    timelines = [0] * len(data[0])

    for line in data:
        for i, c in enumerate(line):
            if c == ".":
                continue

            if c == "^" and timelines[i] != 0:
                counter += 1
                timelines[i - 1] += timelines[i]
                timelines[i + 1] += timelines[i]
                timelines[i] = 0
            elif c == "S":
                timelines[i] = 1

    print(counter)
    return counter, sum(timelines)


def part2() -> None:
    _, timelines = part1()
    print(timelines)


if __name__ == "__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    save_output(new_row=[part1_time, part2_time])
