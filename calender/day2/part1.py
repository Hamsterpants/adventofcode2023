import re

# Define the path to the input file
input = '/workspaces/adventofcode2023/calender/day2/input.txt'
testinput = '/workspaces/adventofcode2023/calender/day2/testinput.txt'

# Define maximum values for each color
MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

# Function to check if a hand is legal based on color counts
def is_legal_hand(h):
    # Compile a regular expression to match color and number pairs
    color_number_pattern = re.compile(r'(\d+) (\w+)')
    
    # Find all matches in the hand
    matches = color_number_pattern.findall(h)
    
    # Initialize counters for each color
    red_count = 0
    green_count = 0
    blue_count = 0
    
    # Iterate through matches to sum up the numbers for each color
    for num, color in matches:
        num = int(num) # Convert the number to an integer
        if color == 'red':
            red_count += num
        elif color == 'green':
            green_count += num
        elif color == 'blue':
            blue_count += num
    
    # Check if any color exceeds its maximum value
    if red_count > MAX_RED or green_count > MAX_GREEN or blue_count > MAX_BLUE:
        return False
    else:
        return True

# Function to check if a round is legal
def is_legal_round(rounds):
    for r in rounds:
        if not(is_legal_hand(r)):
            return False
    return True

# Open the file
with open(input, 'r') as file:
    total_sum = 0

    for line in file:
        # Split the line into parts
        parts = line.split(':')

        # Extract the game ID and convert the integer part to an integer
        game_id = parts[0].strip()
        game_int = int(game_id.split(' ')[1])

        # Extract the rounds
        rounds = parts[1].strip().split(';')

        # Check if the round is legal and add the game integer to the total sum if it is
        if (is_legal_round(rounds)):
            total_sum += game_int

print(total_sum)