n, m, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
graphGun = [[[] for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            graphGun[i][j].append(graph[i][j])


class Player:
    def __init__(self, num, x, y, dir, power, gunPower, point):
        self.num = num
        self.x = x
        self.y = y
        self.dir = dir
        self.power = power
        self.gunPower = gunPower
        self.point = point


players = dict()
for i in range(1, m + 1):
    x, y, d, s = map(int, input().split())
    newPlayer = Player(i, x - 1, y - 1, d, s, 0, 0)
    players[i] = newPlayer


def isRange(x, y):
    return 0 <= x < n and 0 <= y < n


def movePlayer(player):
    currX, currY, currDir = player.x, player.y, player.dir
    nx = currX + dx[currDir]
    ny = currY + dy[currDir]

    if not isRange(nx, ny):
        currDir ^= 2
        nx = currX + dx[currDir]
        ny = currY + dy[currDir]

    player.x = nx
    player.y = ny
    player.dir = currDir

    return player.x, player.y, player.dir


def checkExistPlayer(playerNum, x, y):
    for key, val in players.items():
        if key != playerNum and (x, y) == (val.x, val.y):
            return key

    return -1


def compareGun(player):
    currX, currY = player.x, player.y
    currGunPower = player.gunPower

    graphGun[currX][currY].append(currGunPower)
    player.gunPower = 0

    graphGun[currX][currY] = sorted(graphGun[currX][currY])

    player.gunPower = graphGun[currX][currY].pop()


def processWinner(player):
    compareGun(player)


def processLoser(player):
    currX, currY, currDir = player.x, player.y, player.dir
    currGunPower = player.gunPower

    graphGun[currX][currY].append(currGunPower)

    player.gunPower = 0

    for _ in range(4):
        nx = currX + dx[currDir]
        ny = currY + dy[currDir]
        if isRange(nx, ny) and checkExistPlayer(player.num, nx, ny) == -1:
            player.x = nx
            player.y = ny

            player.dir = currDir

            compareGun(player)
            break

        currDir = (currDir + 1) % 4


totalPoint = [0] * (m + 1)


def fight(newPlayer, existPlayerNum):
    existPlayer = players[existPlayerNum]

    newPlayerTotalPower = newPlayer.power + newPlayer.gunPower
    existPlayerTotalPower = existPlayer.power + existPlayer.gunPower
    diffPower = abs(newPlayerTotalPower - existPlayerTotalPower)

    if newPlayerTotalPower > existPlayerTotalPower:
        losePlayer = existPlayer
        winPlayer = newPlayer

    elif newPlayerTotalPower < existPlayerTotalPower:
        losePlayer = newPlayer
        winPlayer = existPlayer

    else:
        if newPlayer.power > existPlayer.power:
            losePlayer = existPlayer
            winPlayer = newPlayer

        else:
            losePlayer = newPlayer
            winPlayer = existPlayer

    totalPoint[winPlayer.num] += diffPower
    winPlayer.point += diffPower

    processLoser(losePlayer)
    processWinner(winPlayer)


def pro():
    for key, val in players.items():
        nextX, nextY, nextDir = movePlayer(val)

        existPlayerNum = checkExistPlayer(key, nextX, nextY)
        if existPlayerNum == -1:
            compareGun(val)
        else:
            fight(val, existPlayerNum)


for _ in range(k):
    pro()

print(*totalPoint[1:])
