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

def mapper(text):
    mapping = []
    for map in text:
        mapperIndex = 0
        while mapperIndex < int(map[2]):
            mapping.append([int(map[1]) + mapperIndex, int(map[0]) + mapperIndex])
            mapperIndex += 1
    return mapping

allMappings = []
for maps in textList[1:]:
    map = mapper(maps[1:])
    allMappings.append(map)

for map in allMappings:
    print(map)


def loopMap(seed, mapping):
    match = False
    for map in mapping:
        if int(map[0]) == int(seed):
            print(seed, map[1])
            seed = map[1]
            return seed
    # if no return yet, seed is not in mapping, so destination = source
    print(seed, seed)
    return seed

def mapSeeds():
    lowestLocation = 99999999999999999999
    for seed in textList[0][0]:
        inputSeed = seed
        if seed.isnumeric():

            for map in allMappings:

                seed = loopMap(seed, map)
        if str(seed).isnumeric():
            if seed < lowestLocation:
                lowestLocation = seed
        print('\n', inputSeed, seed, '\n')
    print("Lowest location", lowestLocation)


mapSeeds()