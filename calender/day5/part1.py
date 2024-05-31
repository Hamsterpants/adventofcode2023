testinput = '/workspaces/adventofcode2023/calender/day5/testinput.txt'
input = '/workspaces/adventofcode2023/calender/day5/input.txt'

test = 0

file_path = testinput if test else input

seeds = []
maps = []
current_map = None

lowest_location = -1

with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    
    if line.startswith("seeds:"):
        seeds = list(map(int, line.split(":")[1].strip().split()))
    elif line.endswith("map:"):
        current_map = []
        maps.append(current_map)
    elif current_map is not None:
        if line:
            current_map.append(tuple(map(int, line.split())))

def find_location(seed):
    for map in maps:
        for dest_, source_, range_ in map:
            if source_ <= seed < source_ + range_:
                seed = dest_ + (seed - source_)
                break
    return seed

for seed in seeds:
    new_location = find_location(seed)
    if new_location < lowest_location or lowest_location == -1:
        lowest_location = new_location
        
print(lowest_location)