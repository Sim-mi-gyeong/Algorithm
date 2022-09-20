# 감시
# 회전은 항상 90도 / 감시하려고 하는 방향이 가로 또는 세로 방향

# 각 CCTV 마다 / 각 CCTV 가 있는 위치마다 / 방향 조합 중 한 가지를 선정 했을 때 사각지대 Count

import sys
from collections import deque

# 북 동 남 서
nx = [-1, 0, 1, 0]
ny = [0, 1, 0, -1]

input = sys.stdin.readline
n, m = map(int, input().split())
cctv = dict()
print(cctv)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = []

for i in range(n):
    tmp = list(input().split())
    graph.append(tmp)
    for j in range(len(tmp)):
        key = int(tmp[j])
        if 1 <= key <= 5:
            if key not in cctv:
                cctv[key] = [(i, j)]
            else:
                cctv[key].append((i, j))

print(cctv)

# tmp = list(combinations())
# tmp = []
# import copy   # copy.deepcopy()
graphCopy = graph[:]


def watch():
    for key, value in cctv.items():
        print("(key, value) : ", (key, value))
        if key == 1:  # 1번일 때 가능한 방향은 4가지이며, cctv가 1번인 위치에서
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            # 상하좌우
            for val in value:  # 각 위치마다 방향 잡기
                x, y = val[0], val[1]  # 현재 위치
                # 각 위치마다 방향 잡기
                for i in range(4):
                    if i == 0:
                        top(x, y)
                    elif i == 1:
                        down(x, y)
                    elif i == 2:
                        left(x, y)
                    elif i == 3:
                        right(x, y)
                    graphCopy = graph[:]

        elif key == 2:
            # 상하 / 좌우
            directions = [[(-1, 0), (1, 0)], [(0, -1), (0, 1)]]
            for val in value:
                x, y = val[0], val[1]  # 현재 위치
                for i in range(2):
                    if i == 0:
                        top(x, y)
                        down(x, y)
                    elif i == 1:
                        left(x, y)
                        right(x, y)
                    graphCopy = graph[:]

        elif key == 3:
            # 시계방향으로
            # 상우 / 하우 / 하좌 / 상좌
            directions = [
                [(-1, 0), (0, 1)],
                [(1, 0), (0, 1)],
                [(1, 0), (-1, 0)],
                [(-1, 0), (0, -1)],
            ]
            for val in value:
                x, y = val[0], val[1]  # 현재 위치
                for i in range(4):
                    if i == 0:
                        top(x, y)
                        right(x, y)
                    elif i == 1:
                        down(x, y)
                        right(x, y)
                    elif i == 2:
                        down(x, y)
                        left(x, y)
                    elif i == 3:
                        top(x, y)
                        left(x, y)
                    graphCopy = graph[:]

        elif key == 4:
            # 시계방향으로
            # 상좌우 / 상하우 / 하좌우 / 상하좌
            directions = [
                [(-1, 0), (0, -1), (1, 0)],
                [(-1, 0), (1, 0), (0, 1)],
                [(1, 0), (0, -1), (0, 1)],
                [(-1, 0), (1, 0), (0, -1)],
            ]
            for val in value:
                x, y = val[0], val[1]  # 현재 위치
                for i in range(4):
                    if i == 0:
                        top(x, y)
                        left(x, y)
                        right(x, y)
                    elif i == 1:
                        top(x, y)
                        down(x, y)
                        right(x, y)
                    elif i == 2:
                        down(x, y)
                        left(x, y)
                        right(x, y)
                    elif i == 3:
                        top(x, y)
                        down(x, y)
                        left(x, y)

        elif key == 5:
            # 상하좌우 전체
            for val in value:
                for d in range(len(dx)):
                    x, y = val[0], val[1]
                    while 0 <= x < n and 0 <= y < m:
                        if graph[x][y] == "0":
                            graph[x][y] = "#"
                        x += dx[d]
                        y += dy[d]

            top(x, y)
            right(x, y)
            down(x, y)
            left(x, y)
            graphCopy = graph[:]


watch()
minCnt = 1e9


def cctv1():
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # 상하좌우

    # 각 위치에서 cctv1 이 호출되면 -> directions 의 각 원소를 한 번씩
    for val in directions:
        for d in range(len(dx)):
            x, y = val[0], val[1]
            while 0 <= x < n and 0 <= y < m:
                if graph[x][y] == "6":
                    break
                elif graph[x][y] == "0":
                    graph[x][y] = "#"
                x += dx[d]
                y += dy[d]


def top(x, y):  # (x, y) 는 현재 위치
    loc = [-1, 0]
    # 현재 위치 기준으로 위쪽 부분 처리
    while 0 <= x < n and 0 <= y < m:
        if graph[x][y] == "6":
            break
        elif graph[x][y] == "0":
            graph[x][y] = "#"
        x += dx[loc[0]]
        y += dy[loc[1]]


def down(x, y):
    loc = [1, 0]

    while 0 <= x < n and 0 <= y < m:
        if graph[x][y] == "6":
            break
        elif graph[x][y] == "0":
            graph[x][y] = "#"
        x += dx[loc[0]]
        y += dy[loc[1]]


def left(x, y):
    loc = [0, -1]

    while 0 <= x < n and 0 <= y < m:
        if graph[x][y] == "6":
            break
        elif graph[x][y] == "0":
            graph[x][y] = "#"
        x += dx[loc[0]]
        y += dy[loc[1]]


def right(x, y):
    loc = [0, 1]
    while 0 <= x < n and 0 <= y < m:
        if graph[x][y] == "6":
            break
        elif graph[x][y] == "0":
            graph[x][y] = "#"
        x += dx[loc[0]]
        y += dy[loc[1]]


def count():
    global minCnt
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "0" or graph[i][j] == "6":
                cnt += 1
    minCnt = min(minCnt, cnt)


print(minCnt)
