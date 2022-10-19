# 배열 돌리기 2

import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
circleCnt = m // 2
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def rotate():
    startX, endX = 0, n - 1
    startY, endY = 0, m - 1

    new_graph = [[] for _ in range(n)]
    for i in range(n):
        new_graph[i] = graph[i][:]

    for circle in range(circleCnt):
        x, y = startX, startY
        for dir in range(len(dx)):
            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]
                if startX <= nx <= endX and startY <= ny <= endY:
                    graph[nx][ny] = new_graph[x][y]
                    x, y = nx, ny
                else:
                    break

        startX += 1
        endX -= 1
        startY += 1
        endY -= 1


for _ in range(r):
    rotate()

for i in range(n):
    print(*graph[i])
