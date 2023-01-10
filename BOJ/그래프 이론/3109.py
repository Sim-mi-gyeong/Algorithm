# 빵집

import sys

input = sys.stdin.readline

r, c = map(int, input().split())

graph = [list(input()) for _ in range(r)]

# dx = [0, -1, 1]
dx = [-1, 0, 1]
dy = [1, 1, 1]
ans = 0
visited = [[0] * c for _ in range(r)]


def dfs(x, y):
    visited[x][y] = 1
    if y == (c - 1):
        return True

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 1 <= ny < c and not visited[nx][ny] and graph[nx][ny] != "x":
            if dfs(nx, ny):
                return True

    return False


for i in range(r):
    if dfs(i, 0):
        ans += 1

print(ans)
