# Puyo Puyo

from collections import deque
import sys

input = sys.stdin.readline

row, col = 12, 6
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(input().strip()) for _ in range(row)]


def bfs(startX, startY):
    q = deque()
    visited = [[0] * col for _ in range(row)]
    group = []

    visited[startX][startY] = 1
    q.append((startX, startY, graph[startX][startY]))
    group.append((startX, startY))

    while q:
        x, y, color = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny]:
                if graph[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append((nx, ny, graph[nx][ny]))
                    group.append((nx, ny))

    return group


def clear(puyoGroups):
    for puyoGroup in puyoGroups:
        for x, y in puyoGroup:
            graph[x][y] = "."


def fail():
    for j in range(col):
        for i in range(row - 1, -1, -1):
            if graph[i][j] != ".":
                puyo = graph[i][j]
                tmpRow = i
                while tmpRow + 1 < row and graph[tmpRow + 1][j] == ".":
                    graph[tmpRow + 1][j] = puyo
                    graph[tmpRow][j] = "."
                    tmpRow += 1


def solve():
    check = False
    puyoGroups = []
    for i in range(row):
        for j in range(col):
            if graph[i][j] != ".":
                puyoGroup = bfs(i, j)
                if len(puyoGroup) >= 4:
                    puyoGroups.append(puyoGroup)

    if len(puyoGroups) >= 1:
        clear(puyoGroups)
        fail()
        check = True

    return check


result = 0
while True:
    if solve():
        result += 1
    else:
        break

print(result)
