import re

ids = []

with open('games.txt', 'r') as f:
    for id, line in enumerate(f):
        blue = max([int(n) for n in re.findall(r'(\d+) blue', line)])
        red = max([int(n) for n in re.findall(r'(\d+) red', line)])
        green = max([int(n) for n in re.findall(r'(\d+) green', line)])

        if red <= 12 and green <= 13 and blue <= 14:
            ids.append(id+1)
            # print(f'ID: {id+1}, RED: {red}, GREEN: {green}, BLUE: {blue}')

print(sum(ids))