import re

def part1():
    limits = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    result = 0

    with open("./day2/input.txt", "r") as f:
        for line in f:
            ID = int(re.findall(r'\bGame (\d+)\b', line)[0])
            reds = list(map(int, re.findall(r'\b(\d+) red\b', line)))
            greens = list(map(int, re.findall(r'\b(\d+) green\b', line)))
            blues = list(map(int, re.findall(r'\b(\d+) blue\b', line)))

            if(max(reds) <= limits["red"] and 
               max(greens) <= limits["green"] and
               max(blues) <= limits["blue"]):
                result += ID

        print(result)

def part2():
    power_sum = 0
    with open("./day2/input.txt", "r") as f:
        for line in f:
            ID = int(re.findall(r'\bGame (\d+)\b', line)[0])
            reds = list(map(int, re.findall(r'\b(\d+) red\b', line)))
            greens = list(map(int, re.findall(r'\b(\d+) green\b', line)))
            blues = list(map(int, re.findall(r'\b(\d+) blue\b', line)))

            power_sum += max(reds) * max(greens) * max(blues)

        print(power_sum)


#part1()
part2()