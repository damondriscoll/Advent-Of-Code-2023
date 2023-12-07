import re

seeds = []
maps = [[],[],[],[],[],[],[]]

with open('maps.txt', 'r') as f:
    for line in f:
        seeds = [int(s) for s in re.findall(r'\d+', line)]
        break
    f.readline()
    f.readline()

    for map in maps: 
        for line in f:
            if not line.strip():
                break
            info = [int(s) for s in re.findall(r'\d+', line)]
            map.append(info)
        f.readline()

locations = []

for seed in seeds:
    for map in maps:
        for range in map:
            if seed >= range[1] and seed <= range[1] + range[2]:
                seed = range[0] + (seed - range[1])
                break
    locations.append(seed)

print(min(locations))
