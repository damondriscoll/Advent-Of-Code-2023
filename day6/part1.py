time_distances = [
    (56, 499),
    (97, 2210),
    (77, 1097),
    (93, 1440)
]

totals = []

for time, distance in time_distances:
    beaten = 0
    for i in range(time):
        if i * (time - i) > distance:
            beaten += 1
    totals.append(beaten)

result = 1
for score in totals:
    result *= score

print(result)