def getPossibilities(race):
    time = race[0]
    neededDistance = race[1]
    pressTime= 0
    possibilities = 0
    while pressTime < int(time):
        raceTime = int(time)-pressTime


        distance = pressTime * raceTime
        print(distance, pressTime, raceTime)
        if distance > int(neededDistance):
            possibilities+=1


        pressTime+=1

    return possibilities

f = open("day6.txt")
fileMatrix = []

for line in f:
    fileMatrix.append(line.split())

races = [[fileMatrix[0][1], fileMatrix[1][1]], [fileMatrix[0][2], fileMatrix[1][2]],[fileMatrix[0][3], fileMatrix[1][3]],[fileMatrix[0][4], fileMatrix[1][4]]]
oneRace = [fileMatrix[0][1]+fileMatrix[0][2]+fileMatrix[0][3]+fileMatrix[0][4], fileMatrix[1][1]+fileMatrix[1][2]+fileMatrix[1][3]+fileMatrix[1][4]]

productPossibilities = 1
for race in races:
    print(race)
    productPossibilities = productPossibilities *getPossibilities(race)

print(productPossibilities)

print(oneRace)
productPossibilities = 1
productPossibilities = productPossibilities *getPossibilities(oneRace)

print(productPossibilities)


