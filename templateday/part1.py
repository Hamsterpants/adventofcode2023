testinput = '/workspaces/adventofcode2023/calender/dayX/testinput.txt'
input = '/workspaces/adventofcode2023/calender/dayX/input.txt'

test = 0

file_path = testinput if test else input

with open(file_path, 'r') as file:
    lines = file.readlines()