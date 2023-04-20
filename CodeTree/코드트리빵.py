from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

peopleTarget = dict()
peopleCheck = dict()
for i in range(1, m + 1):
    x, y = map(int, input().split())
    peopleTarget[i] = (x - 1, y - 1)
    peopleCheck[i] = False

graphInfo = [[[] for _ in range(n)] for _ in range(n)]


def findTargetCamp(targetX, targetY):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    visited[targetX][targetY] = 1
    q.append((targetX, targetY, 0))

    tmpList = []

    while q:
        x, y, dist = q.popleft()
        if graph[x][y] == 1:
            tmpList.append((x, y, dist))
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != -1:
                visited[nx][ny] = 1
                q.append((nx, ny, dist + 1))

    tmpList.sort(key=lambda x: (x[2], x[0], x[1]))

    return tmpList[0]


def moveTargetConv(num, x, y):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    visited[x][y] = 1
    q.append((x, y, 0, -1))

    while q:
        x, y, dist, dir = q.popleft()
        if (x, y) == peopleTarget[num]:
            return dist, dir

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] != -1:
                visited[nx][ny] = 1

                if dist == 0:
                    q.append((nx, ny, dist + 1, i))
                else:
                    q.append((nx, ny, dist + 1, dir))


def checkFinish():
    flag = False
    cnt = 0
    for key, val in peopleCheck.items():
        if val:
            cnt += 1

    if cnt == m:
        flag = True

    return flag


time = 0
while True:
    if checkFinish():
        break

    time += 1

    afterGraphInfo = [[[] for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for peopleNum in graphInfo[i][j]:
                if peopleCheck[peopleNum]:
                    continue
                dist, nextDir = moveTargetConv(peopleNum, i, j)
                ni = i + dx[nextDir]
                nj = j + dy[nextDir]
                afterGraphInfo[ni][nj].append(peopleNum)

    graphInfo = afterGraphInfo

    for i in range(n):
        for j in range(n):
            for peopleNum in graphInfo[i][j]:
                if peopleTarget[peopleNum] == (i, j):
                    peopleCheck[peopleNum] = True
                    graph[i][j] = -1

    if time > m:
        continue

    campX, campY, dist = findTargetCamp(peopleTarget[time][0], peopleTarget[time][1])
    graphInfo[campX][campY].append(time)
    graph[campX][campY] = -1

print(time)
