from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total = 0


def findGroup(startX, startY, visited, groupNum):
    tmpCnt = 0
    q = deque()

    visited[startX][startY] = 1
    q.append((startX, startY, graph[startX][startY]))
    tmpCnt += 1
    graphInfo[startX][startY] = groupNum

    while q:
        x, y, num = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if num == graph[nx][ny]:
                    visited[nx][ny] = 1
                    q.append((nx, ny, graph[nx][ny]))
                    tmpCnt += 1
                    graphInfo[nx][ny] = groupNum

    return tmpCnt


def addScore():
    score = 0
    for i in range(n):
        for j in range(n):
            for d in range(len(dx)):
                ni = i + dx[d]
                nj = j + dy[d]
                if 0 <= ni < n and 0 <= nj < n and graphInfo[i][j] != graphInfo[ni][nj]:
                    groupANum = graphInfo[i][j]
                    groupBNum = graphInfo[ni][nj]

                    score += (
                        (groupInfo[groupANum][1] + groupInfo[groupBNum][1])
                        * (groupInfo[groupANum][0])
                        * (groupInfo[groupBNum][0])
                    )

    return score // 2


def calScore():
    global total, graphInfo, groupInfo

    graphInfo = [[0] * n for _ in range(n)]
    groupInfo = dict()
    visited = [[0] * n for _ in range(n)]
    groupNum = 1
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                tmpCnt = findGroup(i, j, visited, groupNum)
                if groupNum not in groupInfo:
                    groupInfo[groupNum] = [graph[i][j], tmpCnt]
                    groupNum += 1

    total += addScore()


def rotate_90(graph):
    newGraph = list(map(list, zip(*graph[::-1])))
    return newGraph


def reverseRoate90():
    tmpGraph = [[0] * n for _ in range(n)]

    centerX, centerY = n // 2, n // 2

    for j in range(n):
        tmpGraph[centerX][j] = graph[j][centerY]

    for i in range(n):
        tmpGraph[n - 1 - i][centerY] = graph[centerY][i]

    graph[centerX] = tmpGraph[centerX]
    for i in range(n):
        graph[i][centerY] = tmpGraph[i][centerY]


def rotate90():
    centerX, centerY = n // 2, n // 2
    tmpSize = n // 2

    tmpGraph = [[0] * tmpSize for _ in range(tmpSize)]
    for i in range(centerX):
        for j in range(centerY):
            tmpGraph[i][j] = graph[i][j]
    tmpGraph = rotate_90(tmpGraph)
    for i in range(centerX):
        for j in range(centerY):
            graph[i][j] = tmpGraph[i][j]

    tmpGraph = [[0] * tmpSize for _ in range(tmpSize)]
    for i in range(centerX):
        for j in range(centerY + 1, n):
            tmpGraph[i][j - (centerY + 1)] = graph[i][j]
    tmpGraph = rotate_90(tmpGraph)
    for i in range(centerX):
        for j in range(centerY + 1, n):
            graph[i][j] = tmpGraph[i][j - (centerY + 1)]

    tmpGraph = [[0] * tmpSize for _ in range(tmpSize)]
    for i in range(centerX + 1, n):
        for j in range(centerY):
            tmpGraph[i - (centerX + 1)][j] = graph[i][j]
    tmpGraph = rotate_90(tmpGraph)
    for i in range(centerX + 1, n):
        for j in range(centerY):
            graph[i][j] = tmpGraph[i - (centerX + 1)][j]

    tmpGraph = [[0] * tmpSize for _ in range(tmpSize)]
    for i in range(centerX + 1, n):
        for j in range(centerY + 1, n):
            tmpGraph[i - (centerX + 1)][j - (centerY + 1)] = graph[i][j]
    tmpGraph = rotate_90(tmpGraph)
    for i in range(centerX + 1, n):
        for j in range(centerY + 1, n):
            graph[i][j] = tmpGraph[i - (centerX + 1)][j - (centerY + 1)]


def rotate():
    global graph
    reverseRoate90()
    rotate90()


def pro():
    calScore()
    for _ in range(3):
        rotate()
        calScore()


pro()
print(total)
