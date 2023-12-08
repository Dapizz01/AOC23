def hand_to_key_1(hand):
    card_map = {
        "2": "a",
        "3": "b",
        "4": "c",
        "5": "d",
        "6": "e",
        "7": "f",
        "8": "g",
        "9": "h",
        "T": "i",
        "J": "l",
        "Q": "m",
        "K": "n",
        "A": "o"
    }
    return ''.join([card_map[card] for card in hand["hand"]])


def hand_to_key_2(hand):
    card_map = {
        "J": "a",
        "2": "b",
        "3": "c",
        "4": "d",
        "5": "e",
        "6": "f",
        "7": "g",
        "8": "h",
        "9": "i",
        "T": "l",
        "Q": "m",
        "K": "n",
        "A": "o"
    }
    return ''.join([card_map[card] for card in hand["hand"]])


def classify_hand_1(hands):
    categories = {
        "FiveOAK": [],
        "FourOAK": [],
        "FullHouse": [],
        "ThreeOAK": [],
        "TwoPair": [],
        "OnePair": [],
        "HighCard": []
    }
    for hand in hands:
        labels = {}
        for label in hand["hand"]:
            if label not in labels:
                labels[label] = 1
            else:
                labels[label] += 1
        
        if len(labels) == 1:
            categories["FiveOAK"].append(hand)
        elif len(labels) == 2:
            occ = list(labels.values())
            occ.sort()
            if occ == [1, 4]:
                categories["FourOAK"].append(hand)
            else:
                categories["FullHouse"].append(hand)
        elif len(labels) == 3:
            occ = list(labels.values())
            occ.sort()
            if occ == [1, 1, 3]:
                categories["ThreeOAK"].append(hand)
            else:
                categories["TwoPair"].append(hand)
        elif len(labels) == 4:
            categories["OnePair"].append(hand)
        else:
            categories["HighCard"].append(hand)
    return categories


def classify_hand_2(hands):
    categories = {
        "FiveOAK": [],
        "FourOAK": [],
        "FullHouse": [],
        "ThreeOAK": [],
        "TwoPair": [],
        "OnePair": [],
        "HighCard": []
    }
    for hand in hands:
        j_count = 0
        labels = {}
        for label in hand["hand"]:
            if label == "J":
                j_count += 1
            else:
                if label not in labels:
                    labels[label] = 1
                else:
                    labels[label] += 1
        
        if hand["hand"] == "JJJJJ":
            labels = {"J": 5}
        else:
            labels[max(labels, key=labels.get)] += j_count

        if len(labels) == 1:
            categories["FiveOAK"].append(hand)
        elif len(labels) == 2:
            occ = list(labels.values())
            occ.sort()
            if occ == [1, 4]:
                categories["FourOAK"].append(hand)
            else:
                categories["FullHouse"].append(hand)
        elif len(labels) == 3:
            occ = list(labels.values())
            occ.sort()
            if occ == [1, 1, 3]:
                categories["ThreeOAK"].append(hand)
            else:
                categories["TwoPair"].append(hand)
        elif len(labels) == 4:
            categories["OnePair"].append(hand)
        else:
            categories["HighCard"].append(hand)
    return categories


def part1():
    with open("./day7/input.txt", "r") as f:
        hands = []
        score = 0
        for line in f:
            [hand, bid] = line.split(" ")
            hands.append({
                "hand": hand,
                "bid": int(bid)
            })
        hands_dict = classify_hand_1(hands)
        for type_key in hands_dict:
            hands_dict[type_key] = sorted(hands_dict[type_key], key=hand_to_key_1, reverse=True)
        sorted_hands = [hand for hand in list(hands_dict.values()) if hand != []]
        sorted_hands = [item for sublist in sorted_hands for item in sublist]
        sorted_hands.reverse()
        for index, hand in enumerate(sorted_hands):
            score += hand["bid"] * (index + 1)
        print(score)


def part2():
    with open("./day7/input.txt", "r") as f:
        hands = []
        score = 0
        for line in f:
            [hand, bid] = line.split(" ")
            hands.append({
                "hand": hand,
                "bid": int(bid)
            })
        hands_dict = classify_hand_2(hands)
        for type_key in hands_dict:
            hands_dict[type_key] = sorted(hands_dict[type_key], key=hand_to_key_2, reverse=True)
        sorted_hands = [hand for hand in list(hands_dict.values()) if hand != []]
        sorted_hands = [item for sublist in sorted_hands for item in sublist]
        sorted_hands.reverse()
        for index, hand in enumerate(sorted_hands):
            score += hand["bid"] * (index + 1)
        print(score)


# part1()
part2()