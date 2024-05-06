import re

# Define the path to the input file
input = '/workspaces/adventofcode2023/calender/day2/input.txt'
testinput = '/workspaces/adventofcode2023/calender/day2/testinput.txt'

# Regex pattern to extract number and color pairs
color_number_pattern = re.compile(r'(\d+) (\w+)')

# Function to check if a hand is legal based on color counts
def count_colors(hand):

    # Extract all (number, color) pairs from the hand
    matches = color_number_pattern.findall(hand)
    
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
    
    return red_count, green_count, blue_count

# Function to check if a round is legal
def find_sum(rounds):
    # Initialize minimum counts
    minimum_red_count = 0
    minimum_green_count = 0
    minimum_blue_count = 0

    # Determine minimum counts for each color
    for r in rounds:
        color_counts = count_colors(r)
        red_count = color_counts[0]
        green_count = color_counts[1]
        blue_count = color_counts[2]

        if red_count > minimum_red_count:
            minimum_red_count = red_count
        if green_count > minimum_green_count:
            minimum_green_count = green_count
        if blue_count > minimum_blue_count:
            minimum_blue_count = blue_count

    return (minimum_red_count * minimum_green_count * minimum_blue_count)

# Open the file
with open(testinput, 'r') as file:
    total_sum = 0

    for line in file:
        # Split the line into parts
        parts = line.split(':')

        # Extract the round
        round = parts[1].strip().split(';')

        total_sum += find_sum(round)

print(total_sum)