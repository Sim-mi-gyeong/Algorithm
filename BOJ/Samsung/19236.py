import sys
import copy

input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

graph = [[[0] * 2 for _ in range(4)] for _ in range(4)]
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        graph[i][j // 2][j % 2] = tmp[j]
n = 4


def find_fish(graph, num):
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] == num:
                return (i, j)
    return -1


def move_fish(graph, sharkX, sharkY):
    for num in range(1, 17):
        move_fish_pos = find_fish(graph, num)
        if move_fish_pos != -1:
            x, y = move_fish_pos[0], move_fish_pos[1]
            dir = graph[x][y][1]
            for _ in range(8):
                nx = x + dx[dir - 1]
                ny = y + dy[dir - 1]
                if 0 <= nx < n and 0 <= ny < n:
                    if not (nx == sharkX and ny == sharkY):
                        graph[x][y][1] = dir
                        graph[nx][ny][0], graph[x][y][0] = graph[x][y][0], graph[nx][ny][0]
                        graph[nx][ny][1], graph[x][y][1] = graph[x][y][1], graph[nx][ny][1]
                        break
                dir = (dir + 1) % 8


def move_shark_loc(graph, sharkX, sharkY):
    sharkDir = graph[sharkX][sharkY][1]
    sharkMoveEableList = []
    for i in range(1, 4):
        nextSharkX = sharkX + i * dx[sharkDir - 1]
        nextSharkY = sharkY + i * dy[sharkDir - 1]
        if 0 <= nextSharkX < n and 0 <= nextSharkY < n:
            if 1 <= graph[nextSharkX][nextSharkY][0] <= 16:
                sharkMoveEableList.append((nextSharkX, nextSharkY))

    return sharkMoveEableList


totalVal = 0
maxVal = 0


def dfs(graph, sharkX, sharkY, totalVal):
    global maxVal

    copyGraph = copy.deepcopy(graph)

    tmpVal = copyGraph[sharkX][sharkY][0]
    totalVal += tmpVal
    copyGraph[sharkX][sharkY][0] = -1

    move_fish(copyGraph, sharkX, sharkY)

    sharkMoveEableList = move_shark_loc(copyGraph, sharkX, sharkY)
    if len(sharkMoveEableList) == 0:
        maxVal = max(maxVal, totalVal)
        return

    for nextSharkX, nextSharkY in sharkMoveEableList:
        dfs(copyGraph, nextSharkX, nextSharkY, totalVal)

    graph = copyGraph


dfs(graph, 0, 0, 0)
print(maxVal)
