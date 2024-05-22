testinput = '/workspaces/adventofcode2023/calender/day4/testinput.txt'
input = '/workspaces/adventofcode2023/calender/day4/input.txt'

test = 1

file_path = testinput if test else input

with open(file_path, 'r') as file:
    lines = file.readlines()

def count_frequency(lst1, lst2):
    return sum(1 for x in lst1 if x in lst2)

total_sum = 0
total_match = 0

for line in lines:
    card, numbers = line.split(':')
    left_side, right_side = numbers.split('|')

    winning_numbers = list(map(int, left_side.split()))
    my_numbers = list(map(int, right_side.split()))

    match_count = count_frequency(winning_numbers, my_numbers)
    
    if match_count != 0:
        total_sum += pow(2, match_count-1)

print(total_sum)