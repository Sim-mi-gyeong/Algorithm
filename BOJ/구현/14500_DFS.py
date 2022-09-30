# 테트로미노

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maxTmpVal = max(map(max, graph))
ans = 0


def dfs(x, y, tmpVal, cnt):
    global ans

    if tmpVal + (maxTmpVal) * (4 - cnt) <= ans:
        return

    if cnt == 4:
        ans = max(ans, tmpVal)
        return

    for i in range(len(dx)):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if cnt == 2:
                visited[nx][ny] = 1
                dfs(x, y, tmpVal + graph[nx][ny], cnt + 1)
                visited[nx][ny] = 0

            visited[nx][ny] = 1
            dfs(nx, ny, tmpVal + graph[nx][ny], cnt + 1)
            visited[nx][ny] = 0


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = 1
            dfs(i, j, graph[i][j], 1)
            visited[i][j] = 0


print(ans)
