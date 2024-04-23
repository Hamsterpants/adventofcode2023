import re

input = '/workspaces/adventofcode2023/calender/day1/input.txt'

# Open the file
with open(input, 'r') as file:
    total_sum = 0

    for line in file:
        # Use regex to find all integers in the line
        numbers = re.sub("[^0-9]", "", line)
        first_number = numbers[0]
        last_number = numbers[-1]
        combine = first_number + last_number
        total_sum += int(combine)

print("Total Sum:", total_sum)