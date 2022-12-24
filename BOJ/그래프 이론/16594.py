# 움직이는 미로 탈출

from collections import deque
import sys

input = sys.stdin.readline

graph = deque()
n = 8
for i in range(n):
    tmp = list(input())
    graph.append(tmp)

dx = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 0, 1, 1, 1, 0, -1, -1, -1]

startX, startY = 7, 0
endX, endY = 0, 7


def bfs(startX, startY):
    q = deque()
    q.append((startX, startY))

    # time = 0
    while q:
        visited = [[0] * 8 for _ in range(8)]
        qNum = len(q)
        for _ in range(qNum):
            x, y = q.popleft()

            if (x, y) == (endX, endY):
                return 1

            if graph[x][y] == "#":
                continue

            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] == ".":
                    visited[nx][ny] = 1
                    q.append((nx, ny))

        graph.pop()
        graph.appendleft([".", ".", ".", ".", ".", ".", ".", "."])

        # time += 1
        # if time == 9:
        #     return 1

    return 0


print(bfs(startX, startY))
