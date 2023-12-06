import re

def part1():
    with open("./day6/input2.txt", "r") as f:
        time_limits = []
        min_score = []
        total_wins = 1
        for index, line in enumerate(f):
            if index == 0:
                time_limits = [int(val) for val in re.findall(r'\d+', line)]
            else:
                min_score = [int(val) for val in re.findall(r'\d+', line)]
        for race_index, race_time in enumerate(time_limits):
            wins = 0
            for holding_time in range(0, race_time):
                distance = holding_time * (race_time - holding_time)
                if distance > min_score[race_index]:
                    wins += 1
            total_wins *= wins
        print(total_wins)

part1()
# part2 is part1, just changing the inputs