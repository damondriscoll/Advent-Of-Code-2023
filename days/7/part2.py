from collections import defaultdict

cards = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

strengths = []

with open('hands.txt', 'r') as f:
    for line in f:
        counts = defaultdict(int)
        
        hand, bid = line.split()
        bid = int(bid)

        for card in hand:
            counts[cards.index(card)] += 1

        counts = [[k, v] for k, v in counts.items()]
        counts.sort(key=lambda x: (x[1], x[0]), reverse=True)

        for i, count in enumerate(counts):
            if count[0] == 0 and not count[1] == 5:
                del counts[i]
                counts[0][1] += count[1]
        
        values = [x[1] for x in counts]
        fullhouse = True if 3 in values and 2 in values and 4 not in values else False
        twopairs = True if values.count(2) > 1 and 3 not in values else False

        if fullhouse or twopairs:
            counts[0][1] += 0.5

        strengths.append([counts[0][1]] + [bid, [cards.index(card) for card in hand]])
        
strengths.sort(key=lambda x: (x[0], x[2]))

total = 0
for n in range(len(strengths)):
    total += (n+1) * strengths[n][1]

print(total)