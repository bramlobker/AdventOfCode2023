import re

f = open("day1.txt")
total = 0
part1Total = 0
writtenDigits = [['one', 1], ['two', 2], ['three', 3], ['four', 4], ['five', 5], ['six', 6], ['seven', 7], ['eight', 8], ['nine', 9]]

for line in f:
    digits = []
    digitsPart1 = []
    replacedLine = line

    #Part 2: Use regex to find written digits in text. Determine starting index to sort later (to account for 'oneight'; i save both)
    for digit in writtenDigits:
        pattern = re.compile(digit[0])
        r = pattern.search(line)

        if not r:
            pass

        while r:
            digits.append([digit[1], r.start()])
            r = pattern.search(line, r.start() + 1)

    charCounter = 0;

    #Part 1: Check for each character in line if it is a digit; save digit and index
    for char in line:
        if char.isnumeric():
            digits.append([int(char), int(charCounter)])
            digitsPart1.append([int(char), int(charCounter)])
        charCounter+=1

    #Sort detected digits on index to get first and last
    sortedDigits = sorted(digits, key=lambda l:l[1])
    part1Total += int(str(digitsPart1[0][0])+""+str(digitsPart1[-1][0]))
    total += int(str(sortedDigits[0][0])+""+str(sortedDigits[-1][0]))

print('part 1:', part1Total)
print('part 2:', total)