
testinput = '/workspaces/adventofcode2023/calender/day3/testinput.txt'
input = '/workspaces/adventofcode2023/calender/day3/input.txt'

with open(testinput, 'r') as file:
    lines = file.readlines()

grid = [list(line.strip()) for line in lines]

print(grid[0])
