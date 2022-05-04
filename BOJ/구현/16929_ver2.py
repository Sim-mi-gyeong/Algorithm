# 배열 돌리기1
# deepcopy 보다 리스트 슬라이싱 으로 하는 것이 속도가 더 빠름

import sys

input = sys.stdin.readline

n, m, r = map(int, input().split())  # 행, 열
graph = [list(map(int, input().split())) for _ in range(n)]
# 남 동 북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

nd = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def rotate():
    newGraph = [[] for _ in range(n)]

    for i in range(n):
        newGraph[i] = graph[i][:]  # 배열 복사

    startRow, startCol, endRow, endCol = 0, 0, n - 1, m - 1
    for i in range(int(m / 2)):  # 각 라인별로
        x = startRow
        y = startCol
        for d in nd:  # 남 동 북 서
            while True:
                nx = x + d[0]
                ny = y + d[1]
                if startRow <= nx <= endRow and startCol <= ny <= endCol:
                    graph[nx][ny] = newGraph[x][y]
                    x = nx
                    y = ny
                else:
                    break

        startRow += 1
        startCol += 1
        endRow -= 1
        endCol -= 1


for _ in range(r):
    rotate()

for i in range(n):
    print(*graph[i])
