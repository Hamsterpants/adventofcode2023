import re

testinput = '/workspaces/adventofcode2023/calender/day1/testinput.txt'
input = '/workspaces/adventofcode2023/calender/day1/input.txt'

 # Extended dictionary to include concatenated words
number_words = {
        'oneight': '18', 'sevenine': '79', 'fiveight': '58', 'eighthree': '83', 'twone': '21', 'threeight': '38', 'eightwo': '82',
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
    }

def find_digits(s):
    # Improved pattern to match numeric digits, spelled out numbers, and concatenated words
    pattern = r'\d+|' + '|'.join(number_words.keys())
    
    # Find all matches in the string
    matches = re.findall(pattern, s.lower())
    
    # Convert spelled out numbers and concatenated words to digits
    digits = []
    for match in matches:
        if match.isdigit():
            digits.extend(list(match))  # Extend in case there are multi-digit numbers
        else:
            digits.extend(list(number_words[match]))  # Extend to handle multiple digits from concatenated words
    
    toreturn = digits[0] + digits[-1]

    return toreturn

with open(input, 'r') as file:
    total_sum = 0

    for line in file:
        total_sum += int(find_digits(line))

    print(total_sum)