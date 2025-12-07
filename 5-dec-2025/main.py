# type: ignore
import sys

sys.path.append("..")

from utils import execution_time, read_input, save_output


def part1() -> None:
    data = read_input("input.txt")

    idx = data.index("")

    ranges = data[:idx]
    ingredients = data[idx + 1 :]

    intervals = []
    for r in ranges:
        first, second = r.split("-")
        intervals.append((int(first), int(second)))

    counter = 0
    for ingredient in ingredients:
        number = int(ingredient)
        for first, second in intervals:
            if first <= number <= second:
                counter += 1
                break

    print(counter)


def part2():
    data = read_input("input.txt")
    idx = data.index("")
    data = data[:idx]

    intervals = []
    for r in data:
        first, second = r.split("-")
        intervals.append((int(first), int(second)))

    intervals.sort(key=lambda x: x[0])

    merged = []
    for current in intervals:
        if not merged or merged[-1][1] < current[0] - 1:
            merged.append(current)
        else:
            merged[-1] = (merged[-1][0], max(merged[-1][1], current[1]))

    total = sum(end - start + 1 for start, end in merged)
    print(total)


if __name__ == "__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    print(f"Part 1 execution time: {part1_time:.6f} seconds")
    print(f"Part 2 execution time: {part2_time:.6f} seconds")

    save_output(new_row=[part1_time, part2_time])
