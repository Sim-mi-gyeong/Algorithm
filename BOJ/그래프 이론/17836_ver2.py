from collections import deque
import sys

input = sys.stdin.readline

n, m, t = map(int, input().split())
graph = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j] == 2:
            gramX, gramY = i, j


visited = [[0] * m for _ in range(n)]
gramTime = 1e9


def bfs(startX, startY, visited):
    global gramTime
    q = deque()
    q.append((startX, startY, 0))

    while q:
        x, y, time = q.popleft()
        if x == gramX and y == gramY:
            gramTime = time + abs(n - 1 - gramX) + abs(m - 1 - gramY)
        if x == n - 1 and y == m - 1:
            gramTime = min(gramTime, time)

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                    visited[nx][ny] = 1
                    q.append((nx, ny, time + 1))

    return gramTime


tmpTime = bfs(0, 0, visited)
print(tmpTime if tmpTime <= t else "Fail")

"""
5 4 100
0 1 2 1
0 1 0 1
0 0 0 0
1 1 1 1
0 0 0 0

answer : 11
"""
