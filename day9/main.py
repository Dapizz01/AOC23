def part1():
    with open("./day9/input.txt", "r") as f:
        score = 0
        for line in f:
            history = []
            nums = [int(num) for num in line.split(" ")]
            history.append(nums)
            while not all(el == 0 for el in history[-1]):
                history.append([b - a for a, b in zip(history[-1], history[-1][1:])])
            history[-1].append(0)
            for index in reversed(range(0, len(history) - 1)):
                history[index].append(history[index][-1] + history[index + 1][-1])
            score += history[0][-1]
        print(score)


def part2():
    with open("./day9/input.txt", "r") as f:
        score = 0
        for line in f:
            history = []
            nums = [int(num) for num in line.split(" ")]
            nums.reverse() # Reversing the input is enough, the rest of the code is exactly the same as part1
            history.append(nums)
            while not all(el == 0 for el in history[-1]):
                history.append([b - a for a, b in zip(history[-1], history[-1][1:])])
            history[-1].append(0)
            for index in reversed(range(0, len(history) - 1)):
                history[index].append(history[index][-1] + history[index + 1][-1])
            score += history[0][-1]
        print(score)


# part1()
part2()