import re

def map_seed(seed: int, mappings):
    for mapping in mappings:
        [source, dest, length] = mapping
        if seed >= dest and seed <= dest + length:
            return seed - dest + source
    return seed

def apply_mapping_brute(seed: int, mappings):
    for mapping in mappings:
        if seed >= mapping["dest_base"] and seed <= mapping["dest_base"] + mapping["range"]:
            return seed - mapping["dest_base"] + mapping["source_base"]
    return seed

def apply_mapping(seeds, mappings):
    new_seeds = []
    for mapping in mappings:
        remaining_seeds = []
        for seed in seeds:
            if seed["base"] >= mapping["source_base"] and seed["base"] + seed["range"] <= mapping["source_base"] + mapping["range"]:
                new_seeds.append({
                    "base": mapping["dest_base"] - mapping["source_base"] + seed["base"],
                    "range": seed["range"]
                })
            elif seed["base"] < mapping["source_base"] and seed["base"] + seed["range"] > mapping["source_base"] + mapping["range"]:
                remaining_seeds.append({
                    "base": seed["base"],
                    "range": mapping["source_base"] - seed["base"]
                })
                new_seeds.append({
                    "base": mapping["dest_base"],
                    "range": mapping["range"]
                })
                remaining_seeds.append({
                    "base": mapping["source_base"] + mapping["range"],
                    "range": seed["range"] - mapping["source_base"] - mapping["range"]
                })
            elif seed["base"] < mapping["source_base"] and seed["base"] + seed["range"] >= mapping["source_base"]:
                remaining_seeds.append({
                    "base": seed["base"],
                    "range": mapping["source_base"] - seed["base"]
                })
                new_seeds.append({
                    "base": mapping["dest_base"],
                    "range": seed["base"] + seed["range"] - mapping["source_base"]
                })
            elif seed["base"] <= mapping["source_base"] + mapping["range"] and seed["base"] + seed["range"] > mapping["source_base"] + mapping["range"]:
                remaining_seeds.append({
                    "base": mapping["source_base"] + mapping["range"],
                    "range": seed["base"] + seed["range"] - mapping["source_base"] - mapping["range"]
                })
                new_seeds.append({
                    "base": mapping["dest_base"] - mapping["source_base"] + seed["base"],
                    "range": mapping["source_base"] + mapping["range"] - seed["base"]
                })
            else:
                remaining_seeds.append(seed)
        seeds = remaining_seeds
    return new_seeds + seeds



def part1():
    input_text = ""
    seeds = []
    maps = []
    with open("./day5/input.txt", "r") as f:
        for line in f:
            input_text += line
    input_text = [el for el in input_text.split("\n") if el != ""]
    seeds = [int(seed) for seed in re.findall(r'\d+', input_text[0])]
    for index in range(1, len(input_text)):
        mappings = [int(mapping) for mapping in re.findall(r'\d+', input_text[index])]
        if len(mappings) == 0:
            maps.append([])
        else:
            maps[-1].append(mappings)

    for entry in maps:
        for seed_index, seed in enumerate(seeds):
            seeds[seed_index] = map_seed(seed, entry)

    print(min(seeds))

# To debug, works on test input, not on real input
def part2():
    input_text = ""
    seeds = []
    maps = []
    with open("./day5/input.txt", "r") as f:
        for line in f:
            input_text += line
    paragraphs = [el for el in input_text.split("\n") if el != ""]
    seeds_values = re.findall(r'\d+', paragraphs[0])
    seeds = [{
        "base": int(seeds_values[index]),
        "range" : int(seeds_values[index + 1])
    } for index in range(0, len(seeds_values), 2)]
    for index in range(1, len(paragraphs)):
        raw_mapping = re.findall(r'\d+', paragraphs[index])
        if len(raw_mapping) == 0:
            maps.append([])
        else:
            mappings = {
                "dest_base": int(raw_mapping[0]),
                "source_base": int(raw_mapping[1]),
                "range": int(raw_mapping[2])
            }
            maps[-1].append(mappings)
    for map in maps:
        seeds = apply_mapping(seeds, map)

    # print(seeds)
    print(min(seeds, key=lambda x:x["base"]))


def part2_brute():
    input_text = ""
    seeds = []
    maps = []
    with open("./day5/input.txt", "r") as f:
        for line in f:
            input_text += line
    paragraphs = [el for el in input_text.split("\n") if el != ""]
    seeds_values = re.findall(r'\d+', paragraphs[0])
    seeds = [{
        "base": int(seeds_values[index]),
        "range" : int(seeds_values[index + 1])
    } for index in range(0, len(seeds_values), 2)]
    for index in range(1, len(paragraphs)):
        raw_mapping = re.findall(r'\d+', paragraphs[index])
        if len(raw_mapping) == 0:
            maps.append([])
        else:
            mappings = {
                "dest_base": int(raw_mapping[0]),
                "source_base": int(raw_mapping[1]),
                "range": int(raw_mapping[2])
            }
            maps[-1].append(mappings)
    maps.reverse()
    
    for i in range(1, 10000000000):
        seed = i
        for map in maps:
            seed = apply_mapping_brute(seed, map)
        for seed_range in seeds:
            if seed >= seed_range["base"] and seed <= seed_range["base"] + seed_range["range"]:
                print(i, seed)
                exit()
        if i % 1000000 == 0:
            print("reached ", i)


# part1()
# part2()
part2_brute()