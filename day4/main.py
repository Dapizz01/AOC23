# Given the winning numbers and the other card numbers as lists, returns
# the number of matches (the score)
def card_score(winning_numbers, numbers):
    winning_dict = {}
    score = 0
    for num in winning_numbers:
        winning_dict[num] = 1

    for num in numbers:
        if num in winning_dict:
            score += 1

    return score


# Takes a line from the input as argument, and returns the parsed numbers in it
def card_numbers(card: str):
    winning_numbers = card.split('|')[0].split(':')[1].strip()
    numbers = card.split('|')[1].strip()

    winning_numbers = [int(num) for num in winning_numbers.split()]
    numbers = [int(num) for num in numbers.split()]

    return [winning_numbers, numbers]


def part1():
    with open("./day4/input.txt", "r") as f:
        score_sum = 0
        for line in f:
            [winning_numbers, numbers] = card_numbers(line)
            score = card_score(winning_numbers, numbers)
            score_sum += 0 if score == 0 else pow(2, score - 1)
        print(score_sum)


def part2():
    with open("./day4/input.txt", "r") as f:
        cards = []
        for line in f:
            cards.append(line)
        multiplier = [1 for card in cards] # The number of cards currently holding
        for index, card in enumerate(cards):
            [winning_numbers, numbers] = card_numbers(card)
            score = card_score(winning_numbers, numbers)
            for card_index in range(index + 1, index + score + 1):
                multiplier[card_index] += 1 * multiplier[index] # Add one card times the number of the current card I own
        print(sum(multiplier))
        

# part1()
part2()