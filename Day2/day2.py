from timeit import Timer

rounds = []
with open("input2.txt", "r") as file:
    for item in file.readlines():
        rounds.append(item.strip())


def part1():
    # A X Rock
    # B Y Paper
    # C Z Scissors
    total_score = 0
    points = {"X": 1, "Y": 2, "Z": 3, "loss": 0, "draw": 3, "win": 6}

    for play in rounds:
        opponent, player = play.split(" ")

        total_score += points[player]
        if opponent == "A":
            if player == "X":
                total_score += points["draw"]
            elif player == "Y":
                total_score += points["win"]
            elif player == "Z":
                total_score += points["loss"]
        elif opponent == "B":
            if player == "X":
                total_score += points["loss"]
            elif player == "Y":
                total_score += points["draw"]
            elif player == "Z":
                total_score += points["win"]
        else:
            if player == "X":
                total_score += points["win"]
            elif player == "Y":
                total_score += points["loss"]
            elif player == "Z":
                total_score += points["draw"]

    print(f"Part 1. solution {total_score}")


def part2():
    # A Rock
    # B Paper
    # C Scissor
    # X loss
    # Y draw
    # Z win
    total_score = 0
    points = {"rock": 1, "paper": 2, "scissor": 3, "X": 0, "Y": 3, "Z": 6}

    for play in rounds:
        opponent, outcome = play.split(" ")

        if outcome == "X":
            total_score += points[outcome]
            if opponent == "A":
                total_score += points["scissor"]
            elif opponent == "B":
                total_score += points["rock"]
            elif opponent == "C":
                total_score += points["paper"]
        elif outcome == "Y":
            total_score += points[outcome]
            if opponent == "A":
                total_score += points["rock"]
            elif opponent == "B":
                total_score += points["paper"]
            elif opponent == "C":
                total_score += points["scissor"]
        else:
            total_score += points[outcome]
            if opponent == "A":
                total_score += points["paper"]
            elif opponent == "B":
                total_score += points["scissor"]
            elif opponent == "C":
                total_score += points["rock"]

    print(f"Part 2. solution {total_score}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
