import sys

sys.path.append("..")

from utils import execution_time, read_input, save_output


def remove_roll(grid: list[list[str]]) -> tuple[int, list[list[str]]]:
    N, M = len(grid), len(grid[0])
    new_grid = [row.copy() for row in grid]
    total = 0
    for i, r in enumerate(grid):
        for j, c in enumerate(r):
            if i == 0 and j == 0:
                neighbors = [
                    grid[i][j + 1],
                    grid[i + 1][j],
                    grid[i + 1][j + 1],
                ]
            elif i == 0 and j == M - 1:
                neighbors = [
                    grid[i][j - 1],
                    grid[i + 1][j],
                    grid[i + 1][j - 1],
                ]
            elif i == N - 1 and j == 0:
                neighbors = [
                    grid[i - 1][j],
                    grid[i][j + 1],
                    grid[i - 1][j + 1],
                ]
            elif i == N - 1 and j == M - 1:
                neighbors = [
                    grid[i - 1][j],
                    grid[i][j - 1],
                    grid[i - 1][j - 1],
                ]
            elif i == 0:
                neighbors = [
                    grid[i][j + 1],
                    grid[i][j - 1],
                    grid[i + 1][j],
                    grid[i + 1][j + 1],
                    grid[i + 1][j - 1],
                ]
            elif i == N - 1:
                neighbors = [
                    grid[i][j + 1],
                    grid[i][j - 1],
                    grid[i - 1][j],
                    grid[i - 1][j + 1],
                    grid[i - 1][j - 1],
                ]
            elif j == 0:
                neighbors = [
                    grid[i][j + 1],
                    grid[i + 1][j],
                    grid[i - 1][j],
                    grid[i + 1][j + 1],
                    grid[i - 1][j + 1],
                ]
            elif j == M - 1:
                neighbors = [
                    grid[i][j - 1],
                    grid[i + 1][j],
                    grid[i - 1][j],
                    grid[i + 1][j - 1],
                    grid[i - 1][j - 1],
                ]
            else:
                neighbors = [
                    grid[i][j + 1],
                    grid[i][j - 1],
                    grid[i + 1][j],
                    grid[i - 1][j],
                    grid[i + 1][j + 1],
                    grid[i - 1][j - 1],
                    grid[i + 1][j - 1],
                    grid[i - 1][j + 1],
                ]
            num = neighbors.count("@")
            if num < 4 and c == "@":
                total += 1
                new_grid[i][j] = "."

    return total, new_grid


def part1() -> None:
    input = read_input("example.txt")
    grid = [[str(x) for x in line] for line in input]

    total, _ = remove_roll(grid)
    print(total)


def part2() -> None:
    input = read_input("input.txt")
    grid = [[str(x) for x in line] for line in input]

    total = 0
    while True:
        removed, grid = remove_roll(grid)
        total += removed
        if removed == 0:
            break

    print(total)


if __name__ == "__main__":
    part1_time = execution_time(part1)
    part2_time = execution_time(part2)

    print(f"Part 1 execution time: {part1_time} seconds")
    print(f"Part 2 execution time: {part2_time} seconds")

    save_output(new_row=[part1_time, part2_time])
