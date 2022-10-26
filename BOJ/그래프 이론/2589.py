# 보물섬

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

maxTime = 0


def bfs(startX, startY):
    global maxTime
    q = deque()
    visited = [[0] * m for _ in range(n)]

    q.append((startX, startY, 0))
    visited[startX][startY] = 1

    while q:
        x, y, cnt = q.popleft()
        if (x, y) != (startX, startY) and graph[x][y] == "L":
            maxTime = max(maxTime, cnt)
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == "L":
                    visited[nx][ny] = 1
                    q.append((nx, ny, cnt + 1))


for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            bfs(i, j)
print(maxTime)
