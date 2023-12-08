import re, math

def execute_instructions(map, node: str, instructions: str):
    current_node = node
    ins_index = 0
    steps = 0
    while current_node != "ZZZ":
        current_node = map[current_node][instructions[ins_index]]
        steps += 1
        ins_index += 1
        if ins_index == len(instructions):
            ins_index = 0
    return steps


def execute_instructions2(map, starters: [], instructions: str):
    current_nodes = starters
    ins_index = 0
    steps = 0
    first_z = [-1] * len(current_nodes) # Keeps track of the first "XXZ" like string for each starter
    while elementwise_or(first_z, -1):
        current_nodes = [map[node][instructions[ins_index]] for node in current_nodes]
        steps += 1
        ins_index += 1
        if ins_index == len(instructions):
            ins_index = 0
        # Updates first_z if it has been found a node with a terminal "Z"
        for i in range(0, len(current_nodes)):
            if first_z[i] == -1 and current_nodes[i][-1] == "Z":
                first_z[i] = steps

    # The puzzle description doesn't specify some (very) important things:
    # 1. Every node path contains exactly only one node which ends with "Z"
    # 2. Also, the node paths are closed (it's always the same, there's at least one node that starts and ends the loop)
    # So, we can use the LCM between all the starter nodes to check when they are on the "Z" node at the same time.

    # Thanks to (https://www.reddit.com/r/adventofcode/comments/18djj8h/2023_day_8_part_2_are_you_stuck_and_need_a_hint/)
    return math.lcm(*first_z)


def elementwise_or(l: list, target: int):
    result = False
    for el in l:
        if el == target:
            result = True
    return result


def part1():
    raw_text = ""
    instructions = ""
    map = {}
    with open("./day8/input.txt", "r") as f:
        raw_text = f.readlines()
        instructions = raw_text[0].strip()
        for row in raw_text[2:]:
            [node, left, right] = re.findall(r'[A-Z]+', row)
            map[node] = {
                "L": left,
                "R": right
            }
        print(execute_instructions(map, "AAA", instructions))


def part2():
    raw_text = ""
    instructions = ""
    map = {}
    starters = []
    with open("./day8/input.txt", "r") as f:
        raw_text = f.readlines()
        instructions = raw_text[0].strip()
        for row in raw_text[2:]:
            [node, left, right] = re.findall(r'[A-Z]+', row)
            if node[-1] == "A":
                starters.append(node)
            map[node] = {
                "L": left,
                "R": right
            }
        print(execute_instructions2(map, starters, instructions))


# part1()
part2()