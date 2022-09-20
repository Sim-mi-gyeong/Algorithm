# 탈출

from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

r, c = map(int, input().split())
visited = [[0] * c for _ in range(r)]
graph = []
water = deque()
for i in range(r):
    tmp = list(input())
    graph.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == "S":
            startX, startY = i, j
        if tmp[j] == "*":
            water.append((i, j))


def bfs(graph, startX, startY):
    q = deque()
    q.append((startX, startY, 0))
    visited[startX][startY] = 1
    while q:
        for _ in range(len(water)):
            waterX, waterY = water.popleft()
            for j in range(len(dx)):
                toWaterX = waterX + dx[j]
                toWaterY = waterY + dy[j]
                if (
                    0 <= toWaterX < r
                    and 0 <= toWaterY < c
                    and graph[toWaterX][toWaterY] != "X"
                    and graph[toWaterX][toWaterY] != "D"
                    and graph[toWaterX][toWaterY] != "*"
                ):
                    graph[toWaterX][toWaterY] = "*"
                    water.append((toWaterX, toWaterY))

        for _ in range(len(q)):
            x, y, cnt = q.popleft()
            if graph[x][y] == "D":
                return cnt

            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny]:
                    if graph[nx][ny] == "." or graph[nx][ny] == "D":
                        visited[nx][ny] = 1
                        q.append((nx, ny, cnt + 1))

    return "KAKTUS"


print(bfs(graph, startX, startY))
