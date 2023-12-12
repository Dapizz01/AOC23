def expand_universe(galaxy_map: list, scale: int) -> list:
    galaxies = []
    expanded_galaxies = []
    empty_rows = []
    empty_cols = []

    for index, row in enumerate(galaxy_map):
        if '#' not in row:
            empty_rows.append(index)
    
    for index in range(len(galaxy_map[0])):
        galaxy_col = False
        for row in galaxy_map:
            if row[index] == '#':
                galaxy_col = True
        if galaxy_col == False:
            empty_cols.append(index)

    for y in range(len(galaxy_map)):
        for x in range(len(galaxy_map[0])):
            if galaxy_map[y][x] == '#':
                galaxies.append([y, x])

    for galaxy in galaxies:
        row_offset = 0
        col_offset = 0
        for empty_row in empty_rows:
            if empty_row < galaxy[0]:
                row_offset += 1
        for empty_col in empty_cols:
            if empty_col < galaxy[1]:
                col_offset += 1
        row_offset = row_offset * scale - row_offset
        col_offset = col_offset * scale - col_offset
        expanded_galaxies.append([row_offset + galaxy[0], col_offset + galaxy[1]]) # Manhattan distance

    return expanded_galaxies


def part2():
    with open("./day11/input.txt", "r") as f:
        galaxy_map = []
        galaxies = []
        distance = 0
        for line in f:
            galaxy_map.append([c for c in line.strip()])
        galaxies = expand_universe(galaxy_map, 1000000) # Change to 2 for part1
        for start_index in range(0, len(galaxies)):
            for index in range(start_index, len(galaxies)):
                distance += abs(galaxies[start_index][1] - galaxies[index][1]) + abs(galaxies[start_index][0] - galaxies[index][0])
        print(distance)


# part1 is part2() with a 2 multiplier
part2()