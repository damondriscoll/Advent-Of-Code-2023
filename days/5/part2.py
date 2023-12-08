"""
I was very stuck on this one; I watched this tutorial for help:
https://www.youtube.com/watch?v=NmxHw_bHhGM
"""

import re

seeds = []
maps = [[],[],[],[],[],[],[]]

with open('maps.txt', 'r') as f:
    for line in f:
        seeds = [int(s) for s in re.findall(r'\d+', line)]
        seeds = [(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
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

for map in maps:
    new = []
    while len(seeds) > 0:
        start, end = seeds.pop()
        for destination, source, length in map:
            overlap_start = max(start, source)
            overlap_end = min(end, source + length)
            if overlap_start < overlap_end:
                new.append((overlap_start - source + destination, overlap_end - source + destination))
                if overlap_start > start:
                    seeds.append((start, overlap_start))
                if end > overlap_end:
                    seeds.append((overlap_end, end))
                break
        else:
            new.append((start,end))
    seeds = new

print(min(seeds))



