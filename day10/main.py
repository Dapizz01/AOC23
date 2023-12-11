import sys

pipe_links = {
    "|": ["north", "south"],
    "-": ["west", "east"],
    "L": ["north", "east"],
    "J": ["north", "west"],
    "7": ["south", "west"],
    "F": ["south", "east"],
    ".": [],
    "S": ["north", "east", "south", "west"]
}

pipe_attachments = {
    "north": "|7F",
    "east": "-J7",
    "south": "|LJ",
    "west": "-LF"
}

right_orientation = {
    "north": "right",
    "west": "south",
    "south": "west",
    "west": "north"
}

borders = {
    "|": "│",
    "-": "━",
    "L": "└",
    "J": "┘",
    "7": "┐",
    "F": "┌",
    ".": ".",
    "1": "1",
    "2": "2",
    "S": "S"
}


def dfs(map, y, x, source_dir, print_map) -> int:
    if map[y][x] == "S":
        return 1

    print_map[y][x] = "#"
    next_dir = [d for d in pipe_links[map[y][x]] if d != source_dir]
    next_dir = next_dir[0]

    if next_dir == "north":
        return dfs(map, y - 1, x, "south", print_map) + 1
    elif next_dir == "east":
        return dfs(map, y, x + 1, "west", print_map) + 1
    elif next_dir == "south":
        return dfs(map, y + 1, x, "north", print_map) + 1
    else: # west
        return dfs(map, y, x - 1, "east", print_map) + 1


def dfs_2(map, y, x, source_dir, in_dir, track_map) -> int:
    if map[y][x] == "S":
        return 1

    # This doesn't work on corners, it only checks the first half of it! At least, I think that's why it doesn't work on real input...
    '''
    Ex:  *
        -┐* if the right is on the right side, one should check both the right AND the top, otherwise it's missing tiles inside.
    '''
    if in_dir == "east":
        if track_map[y][x + 1] == ".":
            track_map[y][x + 1] = "1"
    elif in_dir == "south":
        if track_map[y + 1][x] == ".":
            track_map[y + 1][x] = "1"
    elif in_dir == "west":
        if track_map[y][x - 1] == ".":
            track_map[y][x - 1] = "1"
    else:
        if track_map[y - 1][x] == ".":
            track_map[y - 1][x] = "1"

    

    next_dir = [d for d in pipe_links[map[y][x]] if d != source_dir]
    next_dir = next_dir[0]
    next_in_dir = ""

    if next_dir == "north":
        next_in_dir = "east"
    elif next_dir == "east":
        next_in_dir = "south"
    elif next_dir == "south":
        next_in_dir = "west"
    else:
        next_in_dir = "north"

    if map[y][x] in ("7", "L", "J", "F"):
        if next_in_dir == "east":
            if track_map[y][x + 1] == ".":
                track_map[y][x + 1] = "1"
        elif next_in_dir == "south":
            if track_map[y + 1][x] == ".":
                track_map[y + 1][x] = "1"
        elif next_in_dir == "west":
            if track_map[y][x - 1] == ".":
                track_map[y][x - 1] = "1"
        else:
            if track_map[y - 1][x] == ".":
                track_map[y - 1][x] = "1"


    if next_dir == "north":
        return dfs_2(map, y - 1, x, "south", "east", track_map) + 1
    elif next_dir == "east":
        return dfs_2(map, y, x + 1, "west", "south", track_map) + 1
    elif next_dir == "south":
        return dfs_2(map, y + 1, x, "north", "west", track_map) + 1
    else: # west
        return dfs_2(map, y, x - 1, "east", "north", track_map) + 1


def floodfill(map, y, x):
    if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
        return 0
    if map[y][x] == "2" or map[y][x] == "#":
        return 0

    map[y][x] = "2"
    return floodfill(map, y - 1, x) + floodfill(map, y + 1, x) + floodfill(map, y, x - 1) + floodfill(map, y, x + 1) + 1


def part1():
    sys.setrecursionlimit(100000)
    with open("./day10/input.txt", "r") as f:
        map = []
        print_map = []
        start = []
        for line in f:
            map.append(line.strip())
            print_map.append(['.'] * len(line))
        for y in range(0, len(map)):
            for x in range(0, len(map[y])):
                if map[y][x] == "S":
                    start.append(y)
                    start.append(x)
        print_map[start[0]][start[1]] = "S"
        print(dfs(map, start[0] - 1, start[1], "south", print_map)/2)

        # Made just to have an idea on how to do part2
        with open("./day10/path.txt", "w") as f_w:
            for row in print_map:
                f_w.write(''.join(a for a in row) + "\n")


def part2():
    # Find the loop, and mark the used pipes (basically like part1)
    # Convert the unused pipes as '.'
    # Re-run the algo that finds the loop, this time marking the '.' on the (relative) right with 1
    # Flood-fill the 1s with 2s
    # Count the 2s line by line
    sys.setrecursionlimit(100000)
    with open("./day10/input.txt", "r") as f:
        map = []
        track_map = []
        start = []
        tiles = 0
        for line in f:
            map.append(line.strip())
            track_map.append(['.'] * len(line))
        for y in range(0, len(map)):
            for x in range(0, len(map[y])):
                if map[y][x] == "S":
                    start.append(y)
                    start.append(x)
        track_map[start[0]][start[1]] = "#"
        dfs(map, start[0] - 1, start[1], "south", track_map)
        dfs_2(map, start[0] - 1, start[1], "south", "east", track_map)
        for y in range(0, len(track_map)):
            for x in range(0, len(track_map[y])):
                if track_map[y][x] == "1":
                    tiles += floodfill(track_map, y, x)

        print(tiles)

        score = 0
        for y in range(0, len(track_map)):
            for x in range(0, len(track_map[y])):
                if track_map[y][x] == "2":
                    score += 1
        print(score)


        with open("./day10/path.txt", "w", encoding="utf-8") as f_w:
            for row_index, row in enumerate(track_map):
                parsed_row = ""
                for col_index, col in enumerate(row):
                    if col == "#":
                        parsed_row += borders[map[row_index][col_index]]
                    else:
                        parsed_row += borders[col]
                # f_w.write(''.join(a for a in list(map(lambda x: borders[x]), row)) + "\n")
                f_w.write(parsed_row + "\n")


# This was so tiring to debug that I still have to refactor this...
# Also, watchout, the code breaks if the loop touches and edge and the direction
# of the loop is hardcoded, as it's first step.
# part1()
part2()