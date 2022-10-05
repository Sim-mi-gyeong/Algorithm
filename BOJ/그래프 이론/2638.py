# 치즈

from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []
cheeseCnt = 0
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == 1:
            cheeseCnt += 1

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(startX, startY):
    q = deque()
    visited = [[0] * m for _ in range(n)]
    visited[startX][startY] = 1
    q.append((startX, startY))

    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    graph[nx][ny] += 1

    tmpCheeseCnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] >= 3:
                tmpCheeseCnt += 1
                graph[i][j] = 0
            elif 1 <= graph[i][j] < 3:
                graph[i][j] = 1

    return tmpCheeseCnt


time = 0
while True:
    if cheeseCnt == 0:
        break

    tmpCheeseCnt = bfs(0, 0)
    cheeseCnt -= tmpCheeseCnt
    time += 1

print(time)
