import re

instructions, *maps = open('instructions.txt', 'r').read().split('\n')

layout = {}

for map in maps:
    matches = re.findall('[A-Z]+', map)
    layout[matches[0]] = (matches[1], matches[2])
maps.clear()

current = "AAA"
steps = 0
while current != "ZZZ":
    for direction in instructions:
        direction = 0 if direction == "L" else 1
        steps += 1

        current = layout[current][direction]

print(steps)