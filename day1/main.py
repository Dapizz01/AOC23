# Recursively parse the literal digits into proper digits
def parser(line: str):
    # Yeah, there are awkward cases like "oneight", that have to be considered like 18.
    # Don't want to waste time on that...
    words = {
        "one": "1ne",
        "two": "2wo",
        "three": "3ee",
        "four": 4,
        "five": "5e",
        "six": 6,
        "seven": "7en",
        "eight": "8ht",
        "nine": "n9e"
    }
    
    # Using sliding windows of different sizes to check the possible string digits
    for index in range(0, len(line)):
        for window_size in range(3, 6):
            if line[index : index + window_size] in words:
                return parser(line[0 : index] + 
                                       str(words[line[index : index + window_size]]) + 
                                       line[index + window_size :])
    return line

def part1():
    with open(".\day1\input.txt", "r") as f:
        result = 0
        for line in f:
            stack = []
            for c in line:
                if c.isdigit():
                    stack.append(int(c))
            result += stack[0] * 10 + stack[-1]
        print(result)

def part2():
    with open(".\day1\input.txt", "r") as f:
        result = 0
        for line in f:
            parsed_line = parser(line)
            stack = []
            for c in parsed_line:
                if c.isdigit():
                    stack.append(int(c))
            result += stack[0] * 10 + stack[-1]
        print(result)

# part1()
part2()