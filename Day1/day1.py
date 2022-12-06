from timeit import Timer

calories = []
with open("input1.txt", "r") as file:
    for item in file.readlines():
        calories.append(item.strip())

elfs = {}


def part1():
    elf_idx = 1

    for idx in range(len(calories)):
        if calories[idx] == "":
            elf_idx += 1
            continue

        if not elfs.get(elf_idx):
            elfs[elf_idx] = 0

        elfs[elf_idx] += int(calories[idx])

    max_val = max(elfs, key=elfs.get)
    print(f"Part 1. solution {elfs[max_val]}")


def part2():
    calories_top_3 = 0

    for _ in range(3):
        max_val = max(elfs, key=elfs.get)
        calories_top_3 += elfs[max_val]
        del elfs[max_val]

    print(f"Part 2. solution {calories_top_3}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
