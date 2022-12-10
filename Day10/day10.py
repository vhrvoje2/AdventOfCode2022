from timeit import Timer
from math import sqrt, pow

program = []
with open("input10.txt", "r") as file:
    for item in file.readlines():
        program.append(item.strip())

"""with open("day10/test10.txt", "r") as file:
    for item in file.readlines():
        program.append(item.strip())"""


def part1():
    n = 0
    signal_strength = 0
    cycle_count = 0
    register_X = 1

    for line in program:
        try:
            instruction, value = line.split(" ")
            cycle_count += 1
            if cycle_count == 20:
                signal_strength += 20 * register_X
            elif cycle_count % (60 + n * 40) == 0:
                signal_strength += cycle_count * register_X
                n += 1
            cycle_count += 1
            if cycle_count == 20:
                signal_strength += 20 * register_X
            elif cycle_count % (60 + n * 40) == 0:
                signal_strength += cycle_count * register_X
                n += 1
            register_X += int(value)
        except ValueError:
            # noop
            cycle_count += 1
            if cycle_count == 20:
                signal_strength += 20 * register_X
            elif cycle_count % (60 + n * 40) == 0:
                signal_strength += cycle_count * register_X
                n += 1

    print(f"Part 1. solution {signal_strength}")


def print_screen(screen):
    for _ in range(len(screen)):
        print(screen[_])


def part2():
    CRT = [
        ["." for _ in range(40)],
        ["." for _ in range(40)],
        ["." for _ in range(40)],
        ["." for _ in range(40)],
        ["." for _ in range(40)],
        ["." for _ in range(40)],
    ]

    n = 0
    signal_strength = 0
    cycle_count = 0
    register_X = 1

    for line in program:
        try:
            instruction, value = line.split(" ")
            cycle_count += 1
            if cycle_count == 20:
                signal_strength += 20 * register_X
            elif cycle_count % (60 + n * 40) == 0:
                signal_strength += cycle_count * register_X
                n += 1
            cycle_count += 1
            if cycle_count == 20:
                signal_strength += 20 * register_X
            elif cycle_count % (60 + n * 40) == 0:
                signal_strength += cycle_count * register_X
                n += 1
            register_X += int(value)
        except ValueError:
            # noop
            cycle_count += 1
            if cycle_count == 20:
                signal_strength += 20 * register_X
            elif cycle_count % (60 + n * 40) == 0:
                signal_strength += cycle_count * register_X
                n += 1

    print(f"Part 2. solution")
    print_screen(CRT)


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
