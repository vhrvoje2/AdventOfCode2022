from timeit import Timer
from operator import attrgetter

filestructure = []
with open("input7.txt", "r") as file:
    for item in file.readlines():
        filestructure.append(item.strip())

"""with open("day7/test7.txt", "r") as file:
    for item in file.readlines():
        filestructure.append(item.strip())"""

total_disk_space = 70000000
minimum_unused_space = 30000000
delete_candidates = []


class Node(object):
    def __init__(self, name, size, is_dir):
        self.name = name
        self.size = size
        self.is_dir = is_dir
        self.parent = None
        self.children = []

    def __repr__(self):
        return self.name

    def add_child(self, obj):
        self.children.append(obj)


def calculateSize(folder):
    size = 0
    for node in folder.children:
        if node.is_dir:
            calculateSize(node)
        size += node.size

    folder.size = size


def filterDirs(folder):
    size = 0
    if folder.size <= 100000:
        size += folder.size
    for node in folder.children:
        if node.is_dir:
            size += filterDirs(node)

    return size


def chooseDir(folder, used_space):
    if total_disk_space - used_space + folder.size > minimum_unused_space:
        delete_candidates.append(folder)
    for node in folder.children:
        if node.is_dir:
            chooseDir(node, used_space)


def part1():
    root = Node("root", 0, True)
    working_dir = root
    filestructure.pop(0)
    idx = 0

    while idx < len(filestructure):
        line = filestructure[idx]

        if line.startswith("$ ls"):
            idx += 1
        elif line == "$ cd ..":
            working_dir = working_dir.parent
            idx += 1
        elif line.startswith("$ cd"):
            dir_name = line.split(" ")[2].strip()
            for child in working_dir.children:
                if child.name == dir_name:
                    working_dir = child
                    break
            idx += 1
        else:
            if "dir" in line:
                dir_name = line.split(" ")[1].strip()
                node = Node(dir_name, 0, True)
            else:
                size, file = line.split(" ")
                node = Node(file, int(size), False)
            working_dir.add_child(node)
            node.parent = working_dir
            idx += 1

    calculateSize(root)
    solution = filterDirs(root)

    print(f"Part 1. solution {solution}")


def part2():
    root = Node("root", 0, True)
    working_dir = root
    filestructure.pop(0)
    idx = 0

    while idx < len(filestructure):
        line = filestructure[idx]

        if line.startswith("$ ls"):
            idx += 1
        elif line == "$ cd ..":
            working_dir = working_dir.parent
            idx += 1
        elif line.startswith("$ cd"):
            dir_name = line.split(" ")[2].strip()
            for child in working_dir.children:
                if child.name == dir_name:
                    working_dir = child
                    break
            idx += 1
        else:
            if "dir" in line:
                dir_name = line.split(" ")[1].strip()
                node = Node(dir_name, 0, True)
            else:
                size, file = line.split(" ")
                node = Node(file, int(size), False)
            working_dir.add_child(node)
            node.parent = working_dir
            idx += 1

    calculateSize(root)
    chooseDir(root, root.size)

    min_node = min(delete_candidates, key=attrgetter("size"))

    print(f"Part 2. solution {min_node.size}")


print(f"Execution time: {Timer(part1).timeit(number=1)}")
print(f"Execution time: {Timer(part2).timeit(number=1)}")
