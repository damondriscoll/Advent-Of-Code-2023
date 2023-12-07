import re
from collections import defaultdict

symbols = defaultdict(list)
sum = 0

with open('schematic.txt', 'r') as f:
    # obtain locations of symbols {row: [column(s)]}
    for i, line in enumerate(f):
        for match in re.finditer(r'[^\.\d\n]', line):
            symbols[i+1].append(match.start(0))
    
    f.seek(0)

    # check if numbers near to symbols
    for i, line in enumerate(f):
        for match in re.finditer(r'\d+', line):
            for n in range(match.start(0)-1 if match.start(0) > 1 else 0, match.end(0)+1 if match.end(0) < len(line) else len(line)):
                for v in [-1, 0, 1]:
                    if n in symbols[i+1+v]:
                        sum += int(match.group(0))

print(sum)