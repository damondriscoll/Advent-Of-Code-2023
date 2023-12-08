import re
from math import lcm

instructions, *maps = open('instructions.txt', 'r').read().split('\n')

layout = {}
current = []

for map in maps:
    matches = re.findall('[A-Z0-9]+', map)
    layout[matches[0]] = (matches[1], matches[2])
    if matches[0][-1] == "A":
        current.append(matches[0])
maps.clear()

steps = []
count = 0

while current:
    for direction in instructions:
        direction = 0 if direction == "L" else 1
        count += 1

        removes = []
        for i,v in enumerate(current):
            current[i] = layout[v][direction]
            if current[i][-1] == "Z":
                steps.append(count)
                removes.append(i)
        
        for remove in removes:
            del current[remove]
        
        
print(steps)
print(lcm(*steps))