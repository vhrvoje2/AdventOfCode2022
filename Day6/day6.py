from timeit import Timer

data = []
with open("input6.txt", "r") as file:
    for item in file.readlines():
        data.append(item.strip())


def part1():
    datastream = data[0]
    window_size = 4
    for idx in range(0, len(datastream) - 4):
        char_set = set(datastream[idx : idx + window_size])
        if len(char_set) == window_size:
            solution_idx = idx + window_size
            break

    print(f"Part 1. solution {solution_idx}")


def part2():
    datastream = data[0]
    window_size = 14
    for idx in range(0, len(datastream) - 14):
        char_set = set(datastream[idx : idx + window_size])
        if len(char_set) == window_size:
            solution_idx = idx + window_size
            break

    print(f"Part 2. solution {solution_idx}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
