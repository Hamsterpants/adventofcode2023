testinput = '/workspaces/adventofcode2023/calender/day4/testinput.txt'
input = '/workspaces/adventofcode2023/calender/day4/input.txt'

test = 0

file_path = testinput if test else input

with open(file_path, 'r') as file:
    lines = file.readlines()

def count_frequency(lst1, lst2):
    return sum(1 for x in lst1 if x in lst2)

total_sum = 0
line_amount = [1 for _ in lines]

for line_number, line in enumerate(lines):
    card, numbers = line.split(':')
    left_side, right_side = numbers.split('|')

    winning_numbers = list(map(int, left_side.split()))
    my_numbers = list(map(int, right_side.split()))

    match_count = count_frequency(winning_numbers, my_numbers)
    
    if match_count != 0:
        for i in range(match_count):
            line_amount[i + line_number + 1] += line_amount[line_number]

print(sum(line_amount))