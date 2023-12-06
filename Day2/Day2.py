config = [['red', 12, 0],['green', 13, 0],['blue', 14, 0]]
f = open('day2.txt')
totalID = 0
totalPower = 0

for line in f:
    possible = True
    id = int(line.split(":")[0].strip('Game '))
    games = line.split(":")[1].split(";")
    print(id)

    #reset highest count for color each game
    for set in config:
        set[2] =0

    for game in games:
        print(game)
        draws = game.split(',')
        for draw in draws:
            color = draw.split()[1]
            number = draw.split()[0]
            for set in config:
                if color == set[0]:
                    if int(number) > set[1]:
                        possible = False
                    if int(number) > set[2]:
                        set[2] = int(number)
    print(config)
    power = config[0][2] * config[1][2] * config [2][2]
    print(power)
    totalPower+= power

    if possible:
        totalID += id

print(totalPower)
print(totalID)
