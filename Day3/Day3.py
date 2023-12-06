import re

f = open('day3.txt')
fileMatrix = []
fileLinelist = []
for line in f:
    fileLinelist.append(line)

def getNumberIndex(line, matrixLine):
    matches = re.finditer(r'\d+', line)

    for match in matches:
        index = 0
        while index < len(match.group(0)):
            matrixLine[match.start()+index] = match.group(0)
            index+=1
    return matrixLine

def findSymbol(line, fileLinelist, lineIndex, fileMatrix):
    matches = re.finditer(r'[^0-9.]+', line)

    lineTotal = 0
    lineGearTotal = 0
    for match in matches:
        #print("Non-number, Non-period character:", match.group(0), "Starts at index:", match.start())
        prevLine = fileMatrix[lineIndex-1]
        #print(prevLine)
        prevCodes = []
        if prevLine[match.start()].isnumeric():
            #print(prevLine[match.start()])
            prevCodes.append(prevLine[match.start()])
        if prevLine[match.start()+1].isnumeric():
            #print(prevLine[match.start()+1])
            prevCodes.append(prevLine[match.start()+1])
        if prevLine[match.start()-1].isnumeric():
            #print(prevLine[match.start()-1])
            prevCodes.append(prevLine[match.start()-1])
        nextLine = fileMatrix[lineIndex+1]
        #set(prevCodes)
        #print(nextLine)
        nextCodes = []
        if nextLine[match.start()].isnumeric():
            #print(nextLine[match.start()])
            nextCodes.append(nextLine[match.start()])
        if nextLine[match.start()+1].isnumeric():
            #print(nextLine[match.start()+1])
            nextCodes.append(nextLine[match.start()+1])
        if nextLine[match.start()-1].isnumeric():
            #print(nextLine[match.start()-1])
            nextCodes.append(nextLine[match.start()-1])
        currLine= fileMatrix[lineIndex]
        #set(nextCodes)
        #print(currLine)
        currCodes = []
        if currLine[match.start()].isnumeric():
            #print(currLine[match.start()])
            currCodes.append(currLine[match.start()])
        if currLine[match.start()+1].isnumeric():
            #print(currLine[match.start()+1])
            currCodes.append(currLine[match.start()+1])
        if currLine[match.start()-1].isnumeric():
            #print(currLine[match.start()-1])
            currCodes.append(currLine[match.start()-1])
        #set(currCodes)

        linePartCodes = []
        prevCodes = list(set(prevCodes))
        for code in prevCodes:
            linePartCodes.append(code)
            lineTotal+=int(code)

        nextCodes = list(set(nextCodes))
        for code in nextCodes:
            linePartCodes.append(code)
            lineTotal+=int(code)

        currCodes = list(set(currCodes))
        for code in currCodes:
            linePartCodes.append(code)
            lineTotal+=int(code)

        if match.group(0) == "*":
            if len(linePartCodes) == 2:
                print(match.group(0), linePartCodes)
                gearRatio = int(linePartCodes[0]) * int(linePartCodes[1])
                lineGearTotal += gearRatio
        #print(linePartCodes)
    #print(lineTotal)
    return lineTotal, lineGearTotal



for line in fileLinelist:
    matrixLine = []
    for character in line:
        matrixLine.append(character)
    matrixLine = getNumberIndex(line, matrixLine)
    fileMatrix.append(matrixLine)

partnumbers = []
lineIndex =0
totalPartsCode = 0
totalGearRatio = 0
for line in fileLinelist:
    lineTotal, lineGearTotal = findSymbol(line.replace("\n", ""), fileLinelist, lineIndex, fileMatrix)
    lineIndex +=1
    totalPartsCode+= lineTotal
    totalGearRatio+= lineGearTotal

print("Total part code", totalPartsCode)
print("Total gear ratio", totalGearRatio)

