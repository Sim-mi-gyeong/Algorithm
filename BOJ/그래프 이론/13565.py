# 침투

import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

graph = [list(input().rstrip()) for _ in range(m)]
visited = [[0] * n for _ in range(m)]


def bfs(start, end):
    q = deque()
    # visited = [[0] * n for _ in range(m)]
    check = False
    visited[start][end] = 1
    q.append((start, end))
    while q:
        x, y = q.popleft()
        if x == m - 1 and graph[x][y] == "0":
            check = True
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == "0":
                visited[nx][ny] = 1
                q.append((nx, ny))
    return check


check = False
for col in range(n):
    if graph[0][col] == "0":
        if bfs(0, col):
            check = True


if check:
    print("YES")
else:
    print("NO")
