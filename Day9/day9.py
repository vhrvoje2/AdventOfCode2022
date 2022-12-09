from timeit import Timer
from math import sqrt, pow

motions = []
with open("input9.txt", "r") as file:
    for item in file.readlines():
        motions.append(item.strip())

"""with open("day9/test9.txt", "r") as file:
    for item in file.readlines():
        motions.append(item.strip())"""


def calc_distance(head, tail):
    return sqrt(pow(head["x"] - tail["x"], 2) + pow(head["y"] - tail["y"], 2))


def part1():
    moves = [motion.split(" ") for motion in motions]
    head_pos = {"x": 0, "y": 0}
    tail_pos = {"x": 0, "y": 0}
    tail_positions = set()

    for move in moves:
        direction = move[0]
        steps = int(move[1])
        for _ in range(steps):
            if direction == "U":
                head_pos["y"] += 1
                distance = calc_distance(head_pos, tail_pos)
                if distance > 2:
                    tail_pos["x"] = head_pos["x"]
                    tail_pos["y"] = head_pos["y"] - 1
                elif distance == 2:
                    tail_pos["y"] += 1
            elif direction == "D":
                head_pos["y"] -= 1
                distance = calc_distance(head_pos, tail_pos)
                if distance > 2:
                    tail_pos["x"] = head_pos["x"]
                    tail_pos["y"] = head_pos["y"] + 1
                elif distance == 2:
                    tail_pos["y"] -= 1
            elif direction == "L":
                head_pos["x"] -= 1
                distance = calc_distance(head_pos, tail_pos)
                if distance > 2:
                    tail_pos["x"] = head_pos["x"] + 1
                    tail_pos["y"] = head_pos["y"]
                elif distance == 2:
                    tail_pos["x"] -= 1
            elif direction == "R":
                head_pos["x"] += 1
                distance = calc_distance(head_pos, tail_pos)
                if distance > 2:
                    tail_pos["x"] = head_pos["x"] - 1
                    tail_pos["y"] = head_pos["y"]
                elif distance == 2:
                    tail_pos["x"] += 1

            tail_positions.add((tail_pos["x"], tail_pos["y"]))

    print(f"Part 1. solution {len(tail_positions)}")


def part2():
    pass
    # print(f"Part 2. solution {max_scenic_score}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
