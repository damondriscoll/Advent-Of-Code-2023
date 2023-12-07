# works for part1 and part2

import re

num_to_word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

sum = 0
with open('calibrations.txt', 'r') as f:
    for line in f:    
        digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)

        first_digit = num_to_word.index(digits[0])+1 if digits[0] in num_to_word else digits[0]
        last_digit = num_to_word.index(digits[-1])+1 if digits[-1] in num_to_word else digits[-1]

        sum += int(f'{first_digit}{last_digit}')

print(sum)