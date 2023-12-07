time = 56977793
distance = 499221010971440

not_beaten = 0

i = 0
while i < time:
    if i * (time - i) <= distance:
        not_beaten += 1
        i += 1
    else:
        break

i = time
while i > 1:
    if i * (time - i) <= distance:
        not_beaten += 1
        i -= 1
    else:
        break

# honestly i have no clue why i have to +1
print(time - not_beaten + 1)