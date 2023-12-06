def mapSource(seedRange, maps):
    rangeIndeces = []
    mappedSeedRange = []

    for rangeIndex in seedRange:
        rangeStart = rangeIndex[0]
        rangeEnd = rangeIndex[1]

        mappingRanges = []

        # As we are dealing with seed ranges, we also retrieve map ranges
        for map in maps:
            mapMin = int(map[1])
            mapMax = int(map[1]) + int(map[2]) - 1
            mappingRanges.append([mapMin, mapMax])

        # The map ranges are sorted from first to last, based on start index
        mappingRangesSorted = sorted(mappingRanges, key=lambda l: l[1])

        # Seed ranges can also fall outside of available maps. To account for this, fake maps are added before and after the actual maps
        # Fake map after last available map
        mappingRangesSorted.append([int(mappingRangesSorted[-1][1] + 1), 9999999999999])

        # Fake map before first available map
        mappingRangesSorted.append([0, int(mappingRangesSorted[0][0] - 1)])

        mappingRangesSorted = sorted(mappingRangesSorted, key=lambda l: l[1])

        # Check if seed range falls entirely before or after the available maps
        # Completely before any mapping
        if int(rangeStart) < mappingRangesSorted[0][0]:
            rangeIndeces.append([rangeStart, mappingRangesSorted[0][0] - 1])
            rangeStart == mappingRangesSorted[0][0]
        # Completely after any mapping
        if int(rangeStart) > mappingRangesSorted[-1][1]:
            rangeIndeces.append([rangeStart, rangeEnd])

        # If not completely before or after it must be in
        # Following code iterates over all available maps (including fakes) and checks if seed range falls within.
        for mapRange in mappingRangesSorted:

            # Check if lowest index of seed range falls within map
            if mapRange[0] <= int(rangeStart) <= mapRange[1]:

                # Check if highest index of seed range falls within map; seed range completely inside one mapping
                if mapRange[0] <= int(rangeEnd) <= mapRange[1]:

                    rangeIndeces.append([rangeStart, rangeEnd])

                # Else its partly inside one mapping. Make new range that ends at end of map. New starting point is end of map +1
                else:
                    rangeIndeces.append([rangeStart, mapRange[1]])
                    rangeStart = mapRange[1] + 1

    maps = sorted(maps, key=lambda l: l[1])
    for rangeIndex in rangeIndeces:

        for map in maps:
            mapMin = int(map[1])
            mapMax = int(map[1]) + int(map[2])

            if mapMin <= rangeIndex[0] <= mapMax:
                diff = int(rangeIndex[0]) - mapMin
                rangeIndex[0] = int(map[0]) + diff

                diff = int(rangeIndex[1]) - mapMin
                rangeIndex[1] = int(map[0]) + diff
                break

        mappedSeedRange.append([rangeIndex[0], rangeIndex[1]])

    print("out", mappedSeedRange, "\n")
    # if this code is reached, there is no mapping, so destination == source
    return mappedSeedRange


def generateSeeds():
    lowestDestination = 99999999999999
    index = 1
    # textList[0][0][1:] contains all the seeds
    # seeds are retrieved in pairs (starting index + length of range)
    while index < len(textList[0][0][1:]):
        seedPair = [textList[0][0][index], textList[0][0][index + 1]]
        index += 2

        rangeStart = seedPair[0]
        rangeEnd = int(seedPair[0]) + int(seedPair[1])
        rangeIndex = [[int(rangeStart), int(rangeEnd)]]

        for maps in textList:
            if len(maps[1:]) != 0:
                rangeIndex = mapSource(rangeIndex, maps[1:])
        print(rangeIndex)
        for pair in rangeIndex:
            if pair[0] < lowestDestination:
                lowestDestination = pair[0]
    print("Lowest dest", lowestDestination)


f = open('day5.txt')
textList = []
tempList = []
# Split file in different parts (seeds and all the maps)
for line in f:

    if line != "\n":
        tempList.append(line.split())

    if line == "\n":
        textList.append(tempList)
        tempList = []
textList.append(tempList)

generateSeeds()