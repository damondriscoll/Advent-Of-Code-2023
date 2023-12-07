import re

cards_used = 0
win_cards = {}

with open('cards.txt', 'r') as f:
    for i, line in enumerate(f):
        whole = re.findall(r'(\d+)\s|\|', line)
        winning_numbers = whole[:whole.index('')]
        owned_numbers = whole[whole.index('')+1:]

        v = 0
        for n in owned_numbers:
            if n in winning_numbers:
                v += 1
        
        win_cards[i] = v

copies = {n: 1 for n in range(len(win_cards))}

for i in copies:
    v = copies[i]
    while v > 0:
        v -= 1
        cards_used += 1
        for n in range(i+1, i+1+win_cards[i]):
            copies[n] += 1


print(cards_used)