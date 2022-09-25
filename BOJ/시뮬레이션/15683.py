import sys
import copy

input = sys.stdin.readline
n, m = map(int, input().split())

camera = []
graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if 1 <= tmp[j] <= 5:
            camera.append((i, j))


def top(graph, x, y):  # (-1, 0)
    dir = [-1, 0]
    while 0 <= x < n and 0 <= y < m:
        if graph[x][y] == 6:
            break
        if graph[x][y] == 0:
            graph[x][y] = "#"
        x += dir[0]
        y += dir[1]


def down(graph, x, y):
    dir = [1, 0]
    while 0 <= x < n and 0 <= y < m:
        if graph[x][y] == 6:
            break
        if graph[x][y] == 0:
            graph[x][y] = "#"
        x += dir[0]
        y += dir[1]


def left(graph, x, y):
    dir = [0, -1]
    while 0 <= x < n and 0 <= y < m:
        if graph[x][y] == 6:
            break
        if graph[x][y] == 0:
            graph[x][y] = "#"
        x += dir[0]
        y += dir[1]


def right(graph, x, y):
    dir = [0, 1]
    while 0 <= x < n and 0 <= y < m:
        if graph[x][y] == 6:
            break
        if graph[x][y] == 0:
            graph[x][y] = "#"
        x += dir[0]
        y += dir[1]


def cctv1(graph, x, y, cnt):
    # 상 하 좌 우
    if cnt == 0:
        top(graph, x, y)
    elif cnt == 1:
        down(graph, x, y)
    elif cnt == 2:
        left(graph, x, y)
    elif cnt == 3:
        right(graph, x, y)

    return graph


def cctv2(graph, x, y, cnt):
    # 상 하 / 좌 우
    if cnt % 2 == 0:
        top(graph, x, y)
        down(graph, x, y)
    elif cnt % 2 == 1:
        left(graph, x, y)
        right(graph, x, y)

    return graph


def cctv3(graph, x, y, cnt):
    # 상 우 / 우 하 / 하 좌 / 상 좌
    if cnt == 0:
        top(graph, x, y)
        right(graph, x, y)
    elif cnt == 1:
        down(graph, x, y)
        right(graph, x, y)
    elif cnt == 2:
        down(graph, x, y)
        left(graph, x, y)
    elif cnt == 3:
        top(graph, x, y)
        left(graph, x, y)

    return graph


def cctv4(graph, x, y, cnt):
    # 좌 상 우 / 상 우 하 / 좌 하 우 / 상 좌 하
    if cnt == 0:
        top(graph, x, y)
        left(graph, x, y)
        right(graph, x, y)
    elif cnt == 1:
        top(graph, x, y)
        down(graph, x, y)
        right(graph, x, y)
    elif cnt == 2:
        down(graph, x, y)
        left(graph, x, y)
        right(graph, x, y)
    elif cnt == 3:
        top(graph, x, y)
        down(graph, x, y)
        left(graph, x, y)

    return graph


def cctv5(graph, x, y):
    # 상 하 좌 우
    top(graph, x, y)
    down(graph, x, y)
    left(graph, x, y)
    right(graph, x, y)

    return graph


def checkSize(graph):
    size = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 0:
                size += 1
    return size


minVal = 1e9


def backtracking(graph, n=0):
    global minVal

    if minVal == 0:
        return

    if n == len(camera):
        size = checkSize(graph)
        minVal = min(minVal, size)
        return

    startX, startY = camera[n][0], camera[n][1]
    cctv = graph[startX][startY]

    for i in range(4):  # 각 방향 종류(4가지, 혹은 2가지, 1가지 방향 조합) 에 대해 -> CCTV
        copyGraph = copy.deepcopy(graph)  # 이전 연산 결과(CCTV 감시 처리)가 저장된 graph
        # copyGraph = graph[:]
        if cctv == 1:
            backtracking(cctv1(copyGraph, startX, startY, i), n + 1)
        elif cctv == 2:
            backtracking(cctv2(copyGraph, startX, startY, i), n + 1)
        elif cctv == 3:
            backtracking(cctv3(copyGraph, startX, startY, i), n + 1)
        elif cctv == 4:
            backtracking(cctv4(copyGraph, startX, startY, i), n + 1)
        else:
            backtracking(cctv5(copyGraph, startX, startY), n + 1)


if len(camera) == 0:
    print(checkSize(graph))
    exit(0)
else:
    backtracking(graph)
    print(minVal)
