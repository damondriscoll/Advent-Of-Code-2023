import re

sum = 0
with open('calibrations.txt', 'r') as f:
    for line in f:    
        digits = re.findall('\d', line)
        sum += int(f'{digits[0]}{digits[-1]}')

print(sum)