from timeit import Timer

rucksacks = []
with open("input3.txt", "r") as file:
    for item in file.readlines():
        rucksacks.append(item.strip())


def determine_priority(item):
    # Lowercase item types a through z have priorities 1 through 26.
    # Uppercase item types A through Z have priorities 27 through 52.
    if item.islower():
        return ord(item) - 96
    else:
        return ord(item) - 64 + 26


def part1():
    priority_sum = 0

    for items in rucksacks:
        left_compartment = items[: int(len(items) / 2)]
        right_compartment = items[int(len(items) / 2) :]
        common_item = set(left_compartment).intersection(right_compartment).pop()
        priority_sum += determine_priority(common_item)

    print(f"Part 1. solution {priority_sum}")


def part2():
    priority_sum = 0
    for idx in range(0, len(rucksacks), 3):
        common_item = (
            set(rucksacks[idx])
            .intersection(rucksacks[idx + 1])
            .intersection(rucksacks[idx + 2])
            .pop()
        )
        priority_sum += determine_priority(common_item)

    print(f"Part 2. solution {priority_sum}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
