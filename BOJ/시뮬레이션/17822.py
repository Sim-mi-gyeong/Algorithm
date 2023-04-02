# 원판 돌리기
import sys
from collections import deque

input = sys.stdin.readline

n, m, t = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]


def rotate(x, d, k):
    tmp = deque(graph[x - 1])
    if d == 0:
        for _ in range(k):
            tmp.rotate(1)
    else:
        tmp.rotate(-k)

    graph[x - 1] = tmp


def checkExistNum():
    check = False
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                check = True
    return check


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(startX, startY):
    tmpList = []

    q = deque()
    visited[startX][startY] = 1
    q.append((startX, startY))
    tmpList.append((startX, startY))

    while q:
        x, y = q.popleft()
        if y == 0:
            if graph[x][y] == graph[x][m - 1] and graph[x][m - 1] != 0 and not visited[x][m - 1]:
                visited[x][m - 1] = 1
                q.append((x, m - 1))
                tmpList.append((x, m - 1))
        elif y == m - 1:
            if graph[x][y] == graph[x][0] and graph[x][0] != 0 and not visited[x][0]:
                visited[x][0] = 1
                q.append((x, 0))
                tmpList.append((x, 0))

        for d in range(len(dx)):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and graph[nx][ny] != 0:
                if graph[nx][ny] == graph[x][y]:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                    tmpList.append((nx, ny))

    return tmpList


def adjAndEqualNum():
    checkAdjAndEqual = False
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j] != 0:
                tmpList = bfs(i, j)
                if len(tmpList) >= 2:
                    checkAdjAndEqual = True
                    for x, y in tmpList:
                        graph[x][y] = 0

    return checkAdjAndEqual


def calAvg():
    tmpSum = 0
    tmpCnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                tmpCnt += 1
        tmpSum += sum(graph[i])

    avg = tmpSum / tmpCnt
    return avg


def plusAndMinus(avg):
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                continue
            if graph[i][j] > avg:
                graph[i][j] -= 1
            elif graph[i][j] < avg:
                graph[i][j] += 1


def getFinalTotal():
    tmpSum = 0
    for i in range(n):
        tmpSum += sum(graph[i])
    return tmpSum


for turn in range(t):
    visited = [[0] * m for _ in range(n)]
    x, d, k = map(int, input().rstrip().split())

    for i in range(x, n + 1):
        if i % x == 0:
            rotate(i, d, k)
    if checkExistNum():
        check = adjAndEqualNum()
        if not check:
            avg = calAvg()
            plusAndMinus(avg)

total = getFinalTotal()
print(total)
