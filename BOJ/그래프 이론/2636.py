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
    cheese = deque()
    q.append((startX, startY))
    visited[startX][startY] = 1

    tmpCheeseCnt = 0

    while q:
        x, y = q.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                elif graph[nx][ny] == 1:
                    tmpCheeseCnt += 1
                    visited[nx][ny] = 1
                    cheese.append((nx, ny))

    while cheese:
        x, y = cheese.popleft()
        graph[x][y] = 0

    return tmpCheeseCnt


time = 0
meltCheeseList = []
while True:

    if cheeseCnt == 0:
        break

    tmpCheeseCnt = bfs(0, 0)
    meltCheeseList.append(tmpCheeseCnt)
    cheeseCnt -= tmpCheeseCnt

    time += 1

print(time)
print(meltCheeseList[-1])

