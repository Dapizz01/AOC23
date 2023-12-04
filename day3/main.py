# Takes a digit coord, then looks left and right recursively to make the whole number in the engine map
def get_engine_number(engine, row: int, col: int, visited:[]):
    number = engine[row][col]
    visited.append([row, col])

    if col - 1 >= 0:
        if engine[row][col - 1].isdigit():
            if [row, col - 1] not in visited:
                number = get_engine_number(engine, row, col - 1, visited) + number

    if col + 1 < len(engine[row]):
        if engine[row][col + 1].isdigit():
            if [row, col + 1] not in visited:
                number = number +  get_engine_number(engine, row, col + 1, visited)

    return number

def part1():
    engine = [] # Puzzle input
    numbers = [] # Valid numbers
    symbols = [] # Coords of interesting symbols
    visited = [] # Coords of visited digits

    with open("./day3/input.txt", "r") as f:
        for line in f:
            engine.append(line.strip()) # Strips \n

    # Find every symbol that isn't '.'
    for i in range(len(engine)):
        for j in range(len(engine[0])):
            if not engine[i][j].isdigit() and engine[i][j] != '.':
                symbols.append([i, j])

    # For every symbol found, look for the digits nearby and find the whole number
    for [s_i, s_j] in symbols:
        for i in range(max(s_i - 1, 0), min(s_i + 2, len(engine))):
            for j in range(max(s_j - 1, 0), min(s_j + 2, len(engine[0]))):
                if engine[i][j].isdigit() and [i, j] not in visited:
                    numbers.append(int(get_engine_number(engine, i, j, visited)))

    print(sum(numbers))

def part2():
    engine = []
    ratios = []
    gears = [] # Coords of the gears symbols
    visited = []

    with open("./day3/input.txt", "r") as f:
        for line in f:
            engine.append(line.strip()) # Strips \n

    for i in range(len(engine)):
        for j in range(len(engine[0])):
            if engine[i][j] == '*':
                gears.append([i, j])

    for [g_i, g_j] in gears:
        numbers = []
        for i in range(max(g_i - 1, 0), min(g_i + 2, len(engine))):
            for j in range(max(g_j - 1, 0), min(g_j + 2, len(engine[0]))):
                if engine[i][j].isdigit() and [i, j] not in visited:
                    numbers.append(int(get_engine_number(engine, i, j, visited)))
        
        if len(numbers) == 2:
            ratios.append(numbers[0] * numbers[1])

    print(sum(ratios))


# part1()
part2()