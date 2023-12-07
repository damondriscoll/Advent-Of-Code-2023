from collections import defaultdict

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
cards.reverse()

strengths = []

with open('hands.txt', 'r') as f:
    for line in f:
        counts = defaultdict(int)
        
        hand, bid = line.split()
        bid = int(bid)

        for card in hand:
            counts[cards.index(card)] += 1

        values = list(counts.values())
        fullhouse = True if 3 in values and 2 in values and 4 not in values else False
        twopairs = True if values.count(2) > 1 and 3 not in values else False

        counts = [[k, v] for k, v in counts.items()]
        counts.sort(key=lambda x: (x[1], x[0]), reverse=True)

        if fullhouse or twopairs:
            counts[0][1] += 0.5

        strengths.append([counts[0][1]] + [bid, [cards.index(card) for card in hand]])
        
strengths.sort(key=lambda x: (x[0], x[2]))

total = 0
for n in range(len(strengths)):
    total += (n+1) * strengths[n][1]

print(total)