import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

INF = int(1e9)

isAttacked = [[False for _ in range(m)] for _ in range(n)]
lastAttack = [[0 for _ in range(m)] for _ in range(n)]


def isFinish():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                cnt += 1

    return cnt == 1


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


def attack(x, y, power):
    isAttacked[x][y] = 1
    graph[x][y] = max(0, graph[x][y] - power)


def raser(startX, startY, targetX, targetY):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    visited = [[0] * m for _ in range(n)]
    come = [[None] * m for _ in range(n)]

    visited[startX][startY] = 1
    q.append((startX, startY))

    while q:
        x, y = q.popleft()

        for d in range(len(dx)):
            nx = (x + dx[d] + n) % n
            ny = (y + dy[d] + m) % m

            if not visited[nx][ny] and graph[nx][ny] > 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
                come[nx][ny] = (x, y)

    if visited[targetX][targetY] == 0:
        return False

    x, y = targetX, targetY
    while x != startX or y != startY:
        power = graph[startX][startY] // 2
        if (x, y) == (targetX, targetY):
            power = graph[startX][startY]

        attack(x, y, power)

        x, y = come[x][y]

    return True


def bomb(startX, startY, targetX, targetY):
    attack(targetX, targetY, graph[startX][startY])

    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    power = graph[startX][startY] // 2
    for d in range(len(dx)):
        nx = (targetX + dx[d] + n) % n
        ny = (targetY + dy[d] + m) % m

        if (nx, ny) == (startX, startY):
            continue

        if (nx, ny) == (targetX, targetY):
            power = graph[startX][startY]

        attack(nx, ny, power)


for time in range(1, k + 1):
    if isFinish():
        break

    attacker = select_attacker()

    target = select_target()

    graph[attacker[0]][attacker[1]] += n + m

    lastAttack[attacker[0]][attacker[1]] = time

    isAttacked = [[False for _ in range(m)] for _ in range(n)]

    isAttacked[attacker[0]][attacker[1]] = True

    if not raser(attacker[0], attacker[1], target[0], target[1]):
        bomb(attacker[0], attacker[1], target[0], target[1])

    for i in range(n):
        for j in range(m):
            if not isAttacked[i][j] and graph[i][j] > 0:
                graph[i][j] += 1

ans = select_target()
print(graph[ans[0]][ans[1]])
