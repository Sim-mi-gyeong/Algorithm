import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)

isAttacked = [[False for _ in range(m)] for _ in range(n)]

lastAttack = [[0 for _ in range(m)] for _ in range(n)]


def isFinish():
    return False


def select_attacker():
    minV, maxT, minI, minJ = INF, -1, 0, 0

    for sum in range(n + m - 2, -1, -1):
        for j in range(m - 1, -1, -1):
            i = sum - j

            if i < 0 or i >= n:
                continue

            if graph[i][j] <= 0:
                continue

            if minV > graph[i][j]:
                minV, maxT, minI, minJ = graph[i][j], lastAttack[i][j], i, j

            elif minV == graph[i][j] and maxT < lastAttack[i][j]:
                minV, maxT, minI, minJ = graph[i][j], lastAttack[i][j], i, j

    return minI, minJ


def select_target():
    maxV, minT, maxI, maxJ = -1, INF, 0, 0

    for sum in range(n + m - 1):
        for j in range(m):
            i = sum - j

            if i < 0 or i >= n:
                continue

            if graph[i][j] <= 0:
                continue

            if maxV < graph[i][j]:
                maxV, minT, maxI, maxJ = graph[i][j], lastAttack[i][j], i, j

            elif maxV == graph[i][j] and minT > lastAttack[i][j]:
                maxV, minT, maxI, maxJ = graph[i][j], lastAttack[i][j], i, j

    return maxI, maxJ


def raser():
    pass


def bomb():
    pass


for time in range(1, k + 1):
    if isFinish():
        break

    atacker = select_attacker()

    target = select_target()

    graph[atacker[0]][atacker[1]] += n + m

    lastAttack[atacker[0]][atacker[1]] = time

    isAttacked = [[False for _ in range(m)] for _ in range(n)]
    isAttacked[atacker[0]][atacker[1]] = True
