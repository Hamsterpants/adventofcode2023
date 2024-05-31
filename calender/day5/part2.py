#https://tildes.net/~comp.advent_of_code/1cn9/day_5_if_you_give_a_seed_a_fertilizer
testinput = '/workspaces/adventofcode2023/calender/day5/testinput.txt'
input = '/workspaces/adventofcode2023/calender/day5/input.txt'

test = 1

file_path = testinput if test else input

seeds = []
current_seeds = None
maps = []
current_map = None

lowest_location = -1

with open(file_path, 'r') as file:
    lines = file.readlines()

for line in lines:
    line = line.strip()
    
    if line.startswith("seeds:"):
        seed_values = list(map(int, line.split(":")[1].strip().split()))
        if len(seed_values) % 2 != 0:
            raise ValueError("Seed values must be in pairs.")     
        current_seeds = []
        seeds.append(current_seeds)
        for i in range(0, len(seed_values), 2):
            current_seeds.append((seed_values[i], seed_values[i] + seed_values[i+1]))
    

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

def find_range(seed_range, map):
    ss = seed_range[0]
    se = seed_range[1]
    for dest_, source_, range_ in map:
        ms = source_
        me = source_ + range_

        if ss < me or se < ms:
            current_seeds.append(ss, se)
        #elif
        #elif
        #elif
        #elif



    return 1


'''
for seed in seeds:
    new_location = find_location(seed)
    if new_location < lowest_location or lowest_location == -1:
        lowest_location = new_location
'''
if 1:
    current_seeds = []
    seeds.append(current_seeds)
if 1:
    current_seeds.append((11, 22))
    current_seeds.append((22, 33))

print(seed_values)
print(seeds)
print(maps)
print(lowest_location)
