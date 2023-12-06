import re

f = open("day1.txt")
total = 0
writtenDigits = [['one', 1], ['two', 2], ['three', 3], ['four', 4], ['five', 5], ['six', 6], ['seven', 7], ['eight', 8], ['nine', 9]]
replacedFile = []
for line in f:
    digits = []
    replacedLine = line
    print(line.strip('\n'))
    for digit in writtenDigits:
        pattern = re.compile(digit[0])
        r = pattern.search(line)
        if not r:
            pass
        while r:
            digits.append([digit[1], r.start()])
            #print("({0}, {1})".format(digit[0], r.start()))
            r = pattern.search(line, r.start() + 1)

    charCounter = 0;
    for char in line:
        if char.isnumeric():
            digits.append([int(char), int(charCounter)])
        charCounter+=1

    sortedDigits = sorted(digits, key=lambda l:l[1])

    print(sortedDigits, int(str(sortedDigits[0][0])+""+str(sortedDigits[-1][0])))
    total += int(str(sortedDigits[0][0])+""+str(sortedDigits[-1][0]))
print(total)