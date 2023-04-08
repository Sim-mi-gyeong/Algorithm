import copy

n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
killerGraph = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def growth():
    tmpGraph = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 or graph[i][j] == -1:
                continue
            for d in range(len(dx)):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < n and 0 <= nj < n:
                    if 1 <= graph[ni][nj]:
                        tmpGraph[i][j] += 1

    for i in range(n):
        for j in range(n):
            graph[i][j] += tmpGraph[i][j]


def copyTree():

    # tmpGraph = [[0] * n for _ in range(n)]
    tmpGraph = copy.deepcopy(graph)

    for i in range(n):
        for j in range(n):
            treeAmount = graph[i][j]
            tmpCnt = 0
            if graph[i][j] == 0 or graph[i][j] == -1:
                continue
            for d in range(len(dx)):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < n and 0 <= nj < n:
                    if graph[ni][nj] == 0 and killerGraph[ni][nj] == 0:
                        tmpCnt += 1

            if tmpCnt == 0:
                continue

            copyAmount = treeAmount // tmpCnt

            for d in range(len(dx)):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < n and 0 <= nj < n:
                    if graph[ni][nj] == 0 and killerGraph[ni][nj] == 0:
                        tmpGraph[ni][nj] += copyAmount
    return tmpGraph


def findKillerLoc():

    dx2 = [-1, -1, 1, 1]
    dy2 = [-1, 1, 1, -1]

    killX, killY = 0, 0
    killAmount = 0

    for i in range(n):
        for j in range(n):
            tmpCnt = 0
            if graph[i][j] >= 1:
                tmpCnt += graph[i][j]
                for d in range(len(dx2)):
                    startX, startY = i, j
                    for _ in range(k):
                        ni = startX + dx2[d]
                        nj = startY + dy2[d]
                        if not (0 <= ni < n and 0 <= nj < n):
                            break
                        if graph[ni][nj] <= 0:
                            break

                        if graph[ni][nj] >= 1:
                            tmpCnt += graph[ni][nj]
                            startX, startY = ni, nj

                        startX, startY = ni, nj

            if killAmount < tmpCnt:
                killX, killY = i, j
                killAmount = tmpCnt

    return killX, killY, killAmount


total = 0


def killer(targetLoc):
    global total
    dx2 = [-1, -1, 1, 1]
    dy2 = [-1, 1, 1, -1]
    targetLocX, targetLocY, killTreeCount = targetLoc[0], targetLoc[1], targetLoc[2]

    killerGraph[targetLocX][targetLocY] = c
    graph[targetLocX][targetLocY] = 0

    for d in range(len(dx2)):
        i, j = targetLocX, targetLocY
        for _ in range(k):
            ni = i + dx2[d]
            nj = j + dy2[d]

            if not (0 <= ni < n and 0 <= nj < n):
                break
            if graph[ni][nj] == -1:
                break
            if graph[ni][nj] == 0:
                killerGraph[ni][nj] = c
                break

            if graph[ni][nj] >= 1:
                killerGraph[ni][nj] = c
                graph[ni][nj] = 0
                i, j = ni, nj

    total += killTreeCount


def downKiller():
    for i in range(n):
        for j in range(n):
            if killerGraph[i][j] > 0:
                killerGraph[i][j] -= 1


for _ in range(m):
    growth()

    graph = copyTree()

    targetLoc = findKillerLoc()

    downKiller()

    killer(targetLoc)

print(total)
