import re

total = 0

with open('cards.txt', 'r') as f:
    for line in f:
        points = 0

        whole = re.findall(r'(\d+)\s|\|', line)
        winning_numbers = whole[:whole.index('')]
        owned_numbers = whole[whole.index('')+1:]

        
        for n in owned_numbers:
            if n in winning_numbers:
                if not points:
                    points = 1
                else:
                    points *= 2
        
        total += points

print(total)