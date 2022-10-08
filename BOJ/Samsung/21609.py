# 상어 중학교

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
rainbow = []
black = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(n):
        if tmp[j] == 0:
            rainbow.append((i, j))
        elif tmp[j] == -1:
            black.append((i, j))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(startX, startY):
    tmpGroup = []
    rainbowBolck = []
    q = deque()
    q.append((startX, startY, graph[startX][startY]))
    visited[startX][startY] = 1

    if 1 <= graph[startX][startY] <= m:
        groupColor = graph[startX][startY]
    else:
        groupColor = 0
        rainbowBolck.append((startX, startY))

    while q:
        x, y, color = q.popleft()
        if graph[x][y] != -1:
            tmpGroup.append((x, y, color))
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] != -1:
                    if graph[nx][ny] == 0:
                        rainbowBolck.append((nx, ny))
                        visited[nx][ny] = 1
                        q.append((nx, ny, 0))
                    elif groupColor == 0 and 1 <= graph[nx][ny] <= m:
                        visited[nx][ny] = 1
                        groupColor = graph[nx][ny]
                        q.append((nx, ny, groupColor))
                    elif graph[nx][ny] == groupColor:
                        visited[nx][ny] = 1
                        q.append((nx, ny, groupColor))

    for x, y in rainbowBolck:
        visited[x][y] = 0

    tmpGroup = sorted(tmpGroup, key=lambda x: (-x[2], x[0], x[1]))
    rainbowCnt = 0
    for tmp in tmpGroup:
        if tmp[2] == 0:
            rainbowCnt += 1

    return tmpGroup, len(tmpGroup), tmpGroup[0], rainbowCnt


def gravity(graph):
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if graph[i][j] != -1:
                move = graph[i][j]
                while 0 <= i < n - 1:
                    ni = i + 1
                    if graph[ni][j] != -2:
                        break
                    graph[i][j] = -2
                    i = ni
                graph[i][j] = move
    return graph


def reverseRotate90(graph):
    n = len(graph)
    m = len(graph[0])
    newGraph = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            newGraph[m - 1 - j][i] = graph[i][j]

    return newGraph


total = 0
while True:
    group = []
    groupList = []
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and 0 <= graph[i][j] <= m:
                tmpGroup, cnt, center, rainbowCnt = bfs(i, j)

                if cnt >= 2 and center[2] != 0:
                    group.append((cnt, rainbowCnt, center, tmpGroup))

    if len(group) < 1:
        break

    group = sorted(group, key=lambda x: (-x[0], -x[1], -x[2][0], -x[2][1], x[3]))
    maxCntGroup = group[0]

    groupList = maxCntGroup[3]
    for i, j, color in groupList:
        graph[i][j] = -2
    total += len(groupList) ** 2

    graph = gravity(graph)

    graph = reverseRotate90(graph)

    graph = gravity(graph)

print(total)


"""
5 4
1 0 -1 0 0
2 0 -1 0 0
3 0 -1 0 0
4 0 -1 -1 -1
4 4 1 1 1
answer : 58

6 3
1 1 1 0 0 0
1 1 1 0 0 0
1 1 3 0 0 0
0 0 0 2 2 2
0 0 0 2 2 2
0 0 0 2 2 2
answer : 793
"""

