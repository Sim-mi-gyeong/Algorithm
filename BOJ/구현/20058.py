# 마법사 상어와 파이어스톰

from collections import deque
import sys

input = sys.stdin.readline


N, Q = map(int, input().split())
n = 2 ** N
graph = [list(map(int, input().split())) for _ in range(n)]
lst = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def rotate_90(graph):
    new_graph = list(map(list, zip(*graph[::-1])))
    return new_graph


def down_ice(graph):
    tmp_list = []
    for i in range(n):
        for j in range(n):
            tmp_cnt = 0
            for k in range(len(dx)):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < n and 0 <= nj < n:
                    if graph[ni][nj] != 0:
                        tmp_cnt += 1

            if tmp_cnt < 3:
                tmp_list.append((i, j))

    for x, y in tmp_list:
        if graph[x][y] >= 1:
            graph[x][y] -= 1

    return graph


for q in range(Q):
    L = lst[q]
    size = 2 ** L
    new_graph = [[0] * n for _ in range(n)]

    startX, endX = 0, size
    while startX != n:
        startY, endY = 0, size
        while startY != n:
            tmp_graph = [[0] * size for _ in range(size)]
            for i in range(startX, endX):
                for j in range(startY, endY):
                    tmp_graph[i - startX][j - startY] = graph[i][j]

            tmp_graph = rotate_90(tmp_graph)
            for i in range(startX, endX):
                for j in range(startY, endY):
                    new_graph[i][j] = tmp_graph[i - startX][j - startY]

            startY, endY = startY + size, endY + size
        startX, endX = startX + size, endX + size

    graph = down_ice(new_graph)


total = 0
for i in range(n):
    for j in range(n):
        total += graph[i][j]

print(total)


visited = [[0] * n for _ in range(n)]


def bfs(startX, startY):
    queue = deque()
    queue.append((startX, startY))
    visited[startX][startY] = 1
    cnt = 1

    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if graph[nx][ny] > 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny))

    return cnt


max_val = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] > 0 and not visited[i][j]:
            tmp_val = bfs(i, j)
            max_val = max(max_val, tmp_val)


print(max_val)
