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

check = False


def bfs(startX, startY, visited):
    global check
    q = deque()
    q.append((startX, startY, 0))

    while q:
        x, y, time = q.popleft()
        if x == gramX and y == gramY:
            gramTime = time + abs(n - 1 - gramX) + abs(m - 1 - gramY)
            if gramTime <= t:
                return gramTime
        if x == n - 1 and y == m - 1:
            if time <= t:
                return time

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, time + 1))
                # elif graph[nx][ny] == 2:
                #     # 그람을 찾은 경우 -> 그 위치에서 바로 탐색하도록
                #     check = True
                #     visited[nx][ny] == 1
                #     q.appendleft((nx, ny, time + 1))
                # elif graph[nx][ny] == 1 and check:
                #     visited[nx][ny] == 1
                #     q.append((nx, ny, time + 1))

    return "Fail"


print(bfs(0, 0, visited))


"""
3 3 1
0 1 0
2 1 0
0 1 0

answer : Fail
"""

