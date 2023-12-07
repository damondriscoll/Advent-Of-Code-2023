import re

powers = []

with open('games.txt', 'r') as f:
    for id, line in enumerate(f):
        blue = max([int(n) for n in re.findall(r'(\d+) blue', line)])
        red = max([int(n) for n in re.findall(r'(\d+) red', line)])
        green = max([int(n) for n in re.findall(r'(\d+) green', line)])

        powers.append(blue * red * green)

print(sum(powers))