f = open('day5.txt')
textList = []
tempList = []
for line in f:

    if line != "\n":
        tempList.append(line.split())

    if line == "\n":
        textList.append(tempList)
        tempList = []
textList.append(tempList)


def mapSource(seed, maps):
    #print(maps)
    for map in maps:
        mapMin = int(map[1])
        mapMax = int(map[1]) + int(map[2]) - 1

        if mapMin <= int(seed) <= mapMax:
            diff = int(seed) - mapMin
            destination = int(map[0]) + diff
            return destination

    # if this code is reached, there is no mapping, so destination == source
    return seed

def generateSeeds():
    lowestDestination = 99999999999999
    index = 1
    while index < len(textList[0][0][1:]):
        seedPair = [textList[0][0][index], textList[0][0][index+1]]
        index +=2

        rangeIndex =0
        seedRange = []
        while rangeIndex < int(seedPair[1]):
            seedRange.append(int(seedPair[0])+rangeIndex)
            rangeIndex+=1

        print(seedPair)

        for seed in seedRange:
            originalSeed = seed
            for maps in textList:
                if len(maps[1:]) != 0:
                    seed = mapSource(seed, maps[1:])
            #print(originalSeed, seed)
            if seed < lowestDestination:
                lowestDestination = seed
    print(lowestDestination)

lowestDestination = 99999999999999
for seed in textList[0][0][1:]:
    originalSeed = seed
    for maps in textList:
        if len(maps[1:]) != 0:
            seed =mapSource(seed, maps[1:])
    print(originalSeed, seed)
    if seed < lowestDestination:
        lowestDestination = seed

print(lowestDestination)
#generateSeeds()








