from timeit import Timer

assignments = []
with open("input4.txt", "r") as file:
    for item in file.readlines():
        assignments.append(item.strip())


def part1():
    counter = 0

    for pair in assignments:
        elf1, elf2 = pair.split(",")
        elf1_start, elf1_end = elf1.split("-")
        elf2_start, elf2_end = elf2.split("-")
        elf1 = [x for x in range(int(elf1_start), int(elf1_end) + 1)]
        elf2 = [x for x in range(int(elf2_start), int(elf2_end) + 1)]

        if len(elf1) > len(elf2):
            if set(elf2).issubset(set(elf1)):
                counter += 1
        else:
            if set(elf1).issubset(set(elf2)):
                counter += 1

    print(f"Part 1. solution {counter}")


def part2():
    counter = 0

    for pair in assignments:
        elf1, elf2 = pair.split(",")
        elf1_start, elf1_end = elf1.split("-")
        elf2_start, elf2_end = elf2.split("-")
        elf1 = [x for x in range(int(elf1_start), int(elf1_end) + 1)]
        elf2 = [x for x in range(int(elf2_start), int(elf2_end) + 1)]

        if set(elf1).intersection(set(elf2)):
            counter += 1

    print(f"Part 2. solution {counter}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
