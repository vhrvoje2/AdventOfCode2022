from timeit import Timer

moves = []
with open("input5.txt", "r") as file:
    for item in file.readlines():
        moves.append(item.strip())

stacks_test = {"1": ["Z", "N"], "2": ["M", "C", "D"], "3": ["P"]}


def part1():
    """
            [J]         [B]     [T]
            [M] [L]     [Q] [L] [R]
            [G] [Q]     [W] [S] [B] [L]
    [D]     [D] [T]     [M] [G] [V] [P]
    [T]     [N] [N] [N] [D] [J] [G] [N]
    [W] [H] [H] [S] [C] [N] [R] [W] [D]
    [N] [P] [P] [W] [H] [H] [B] [N] [G]
    [L] [C] [W] [C] [P] [T] [M] [Z] [W]
    1   2   3   4   5   6   7   8   9
    """
    stacks = {
        "1": ["L", "N", "W", "T", "D"],
        "2": ["C", "P", "H"],
        "3": ["W", "P", "H", "N", "D", "G", "M", "J"],
        "4": ["C", "W", "S", "N", "T", "Q", "L"],
        "5": ["P", "H", "C", "N"],
        "6": ["T", "H", "N", "D", "M", "W", "Q", "B"],
        "7": ["M", "B", "R", "J", "G", "S", "L"],
        "8": ["Z", "N", "W", "G", "V", "B", "R", "T"],
        "9": ["W", "G", "D", "N", "P", "L"],
    }

    for line in moves:
        line = line.split("from")
        crate_count = int(line[0].split("move")[1])
        stack_from = line[1].split("to")[0].strip()
        stack_to = line[1].split("to")[1].strip()

        while crate_count > 0:
            moved_crate = stacks[stack_from].pop()
            stacks[stack_to].append(moved_crate)
            crate_count -= 1

    solution = "".join([stacks[k].pop() for k, v in stacks.items()])
    print(f"Part 1. solution {solution}")


def part2():
    """
            [J]         [B]     [T]
            [M] [L]     [Q] [L] [R]
            [G] [Q]     [W] [S] [B] [L]
    [D]     [D] [T]     [M] [G] [V] [P]
    [T]     [N] [N] [N] [D] [J] [G] [N]
    [W] [H] [H] [S] [C] [N] [R] [W] [D]
    [N] [P] [P] [W] [H] [H] [B] [N] [G]
    [L] [C] [W] [C] [P] [T] [M] [Z] [W]
    1   2   3   4   5   6   7   8   9
    """
    stacks = {
        "1": ["L", "N", "W", "T", "D"],
        "2": ["C", "P", "H"],
        "3": ["W", "P", "H", "N", "D", "G", "M", "J"],
        "4": ["C", "W", "S", "N", "T", "Q", "L"],
        "5": ["P", "H", "C", "N"],
        "6": ["T", "H", "N", "D", "M", "W", "Q", "B"],
        "7": ["M", "B", "R", "J", "G", "S", "L"],
        "8": ["Z", "N", "W", "G", "V", "B", "R", "T"],
        "9": ["W", "G", "D", "N", "P", "L"],
    }

    for line in moves:
        line = line.split("from")
        crate_count = int(line[0].split("move")[1])
        stack_from = line[1].split("to")[0].strip()
        stack_to = line[1].split("to")[1].strip()

        crates_to_move = []

        while crate_count > 0:
            crates_to_move.insert(0, stacks[stack_from].pop())
            crate_count -= 1

        stacks[stack_to].extend(crates_to_move)

    solution = "".join([stacks[k].pop() for k, v in stacks.items()])

    print(f"Part 2. solution {solution}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
