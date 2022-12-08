from timeit import Timer

data = []
with open("input8.txt", "r") as file:
    for item in file.readlines():
        data.append(item.strip())

"""with open("day8/test8.txt", "r") as file:
    for item in file.readlines():
        data.append(item.strip())"""

forest = []

for line in data:
    curr_line = []
    for tree in line:
        curr_line.append(int(tree))
    forest.append(curr_line)


def part1():
    outside_trees = 2 * len(forest) + 2 * (len(forest) - 2)
    visible = 0

    for y in range(1, len(forest) - 1):
        for x in range(1, len(forest) - 1):
            visible_N = visible_S = visible_E = visible_W = True
            current_tree = forest[y][x]

            for n in range(0, y):
                if forest[n][x] >= current_tree:
                    visible_N = False

            for s in range(y + 1, len(forest)):
                if forest[s][x] >= current_tree:
                    visible_S = False

            for w in range(0, x):
                if forest[y][w] >= current_tree:
                    visible_W = False

            for e in range(x + 1, len(forest)):
                if forest[y][e] >= current_tree:
                    visible_E = False

            if any([visible_N, visible_S, visible_E, visible_W]):
                visible += 1

    solution = outside_trees + visible
    print(f"Part 1. solution {solution}")


def part2():
    solution = None
    print(f"Part 2. solution {solution}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
# print(f"Execution time: {Timer(part2).timeit(number=1)}")
