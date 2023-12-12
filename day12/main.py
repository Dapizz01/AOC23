from functools import cache

@cache
def arrangements(record: str, groups:tuple[int, ...]) -> int:
    if len(groups) == 0:
        if '#' in record:
            return 0
        return 1

    next_groups_len = sum(groups[1:]) + len(groups[1:])
    total = 0
    for i in range(len(record) - next_groups_len - groups[0] + 1):
        arrangement = "." * i + "#" * groups[0] + "."
        if all(r == possible_r or r == "?" for r, possible_r in zip(record, arrangement)):
            total += arrangements(record[len(arrangement):], groups[1:])
    return total


def part1():
    with open("./day12/sample_input.txt", "r") as f:
        total_arrangements = 0
        for line in f:
            record, group = line.strip().split(" ")
            group = [int(digit) for digit in group.split(",")]
            total_arrangements += arrangements(record, tuple(group))
        print(total_arrangements)


def part2():
    with open("./day12/input.txt", "r") as f:
        total_arrangements = 0
        for line in f:
            record, group = line.strip().split(" ")
            record = '?'.join([record] * 5)
            group = [int(digit) for digit in group.split(",")] * 5
            total_arrangements += arrangements(record, tuple(group))
        print(total_arrangements)


# To be honest, I couldn't come up with a solution on my own for this one, except brute force.
# I took (huge) inspiration for the idea from the AoC subreddit, in the solutions megathread.
# Needless to say, all off the merit goes to the OP of the post.
# To be even more honest, it took me about half an hour to get why this algo works.
# I got the stars, but not the glory.


# part1()
part2()