# 움직이는 미로 탈출

from collections import deque
import sys

input = sys.stdin.readline

graph = []
wall = deque()
n = 8
for i in range(n):
    tmp = list(input())
    graph.append(tmp)
    for j in range(n):
        if tmp[j] == "#":
            wall.append((i, j))

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

startX, startY = 7, 0
endX, endY = 0, 7


def bfs(startX, startY):
    q = deque()
    visited = [[0] * 8 for _ in range(8)]
    q.append((startX, startY, 0))
    visited[startX][startY] = 1

    while q:
        x, y, time = q.popleft()
        if (x, y) == (endX, endY):
            return 1
        if graph[x][y] == "#":
            return 0

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == ".":
                visited[nx][ny] = 1
                q.append((nx, ny, time + 1))

        wallNum = len(wall)
        for _ in range(wallNum):
            wallX, wallY = wall.popleft()
            if 0 <= wallX + 1 < n:
                graph[wallX + 1][wallY] = "#"
                graph[wallX][wallY] = "."
                wall.append((wallX + 1, wallY))
            else:
                continue

    return 0


print(bfs(startX, startY))
