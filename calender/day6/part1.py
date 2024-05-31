testinput = '/workspaces/adventofcode2023/calender/day6/testinput.txt'
input = '/workspaces/adventofcode2023/calender/day6/input.txt'

test = 1

file_path = testinput if test else input

def read_values_from_file(file_p):
    with open(file_p, 'r') as file:
        lines = file.readlines()

    time_values = []
    distance_values = []

    for line in lines:
        if line.startswith("Time:"):
            time_values = list(map(int, line.split()[1:]))
        elif line.startswith("Distance:"):
            distance_values = list(map(int, line.split()[1:]))

    return time_values, distance_values

def calculate_distance(hold, max_value):
    return hold * (1 + max_value - hold)


time_values, distance_values = read_values_from_file(file_path)

print(f"Time values: {time_values}")
print(f"Distance values: {distance_values}")