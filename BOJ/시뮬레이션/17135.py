# 캐슬 디펜스

import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

n, m, d = map(int, input().rstrip().split())

graph = []
enemyCnt = 0
for i in range(n):
    tmp = list(map(int, input().rstrip().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == 1:
            enemyCnt += 1

ans = 0
huterLocList = [(n, j) for j in range(m)]
combList = list(combinations(huterLocList, 3))

dx = [0, -1, 0]
dy = [-1, 0, 1]


def findEnyme(hunterX, hunterY):
    visited = [[0] * m for _ in range(n)]
    q = deque()

    visited[hunterX - 1][hunterY] = 1
    q.append((hunterX - 1, hunterY))

    while q:
        x, y = q.popleft()
        if getDistance(hunterX, hunterY, x, y) > d:
            return False

        if getDistance(hunterX, hunterY, x, y) <= d and newGraph[x][y] == 1:
            return (x, y)

        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))


def moveEnyme():
    for j in range(m):
        for i in range(n - 2, -1, -1):
            newGraph[i + 1][j] = newGraph[i][j]
    for j in range(m):
        newGraph[0][j] = 0


def checkArriveEnyme():
    arriveEnymeCnt = 0
    for j in range(m):
        if newGraph[n - 1][j] == 1:
            arriveEnymeCnt += 1
    return arriveEnymeCnt


def check(tmpEnemyCnt):
    if tmpEnemyCnt == 0:
        return True
    return False


def getDistance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def solve(comb):
    global newGraph
    cnt = 0
    tmpEnemyCnt = enemyCnt
    newGraph = copy.deepcopy(graph)
    while True:
        if check(tmpEnemyCnt):
            break

        tmpEnemyLoc = set()

        for hunter in comb:
            hunterX, hunterY = hunter[0], hunter[1]
            enymeLoc = findEnyme(hunterX, hunterY)
            if enymeLoc:
                tmpEnemyLoc.add(enymeLoc)

        for tmpEnymeX, tmpEnymeY in tmpEnemyLoc:
            newGraph[tmpEnymeX][tmpEnymeY] = 0

        cnt += len(tmpEnemyLoc)
        tmpEnemyCnt -= len(tmpEnemyLoc)
        tmpEnemyCnt -= checkArriveEnyme()

        moveEnyme()

    return cnt


for comb in combList:
    tmpVal = solve(comb)
    ans = max(ans, tmpVal)

print(ans)
