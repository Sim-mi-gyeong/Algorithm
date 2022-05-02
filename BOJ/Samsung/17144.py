# 미세먼지 안녕!
from copy import deepcopy
import sys

input = sys.stdin.readline
r, c, t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(r)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
newGraph = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(2)]

clear = []
for i in range(r):
    for j in range(c):
        newGraph[0][i][j] = graph[i][j]
        if graph[i][j] == -1:
            clear.append((i, j))
clear.sort(key=lambda x: (x[0], x[1]))
clearUp, clearDown = clear[0], clear[1]

for _ in range(t):
    for i in range(r):
        for j in range(c):
            if newGraph[0][i][j] != 0 and newGraph[0][i][j] != -1:
                staub = newGraph[0][i][j]
                staubDiv = staub // 5
                newGraph[1][i][j] = staubDiv

    for i in range(r):
        for j in range(c):
            if newGraph[0][i][j] != -1:
                divCnt = 0
                for d in range(len(dx)):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if 0 <= nx < r and 0 <= ny < c and newGraph[0][nx][ny] != -1:
                        newGraph[0][nx][ny] += newGraph[1][i][j]
                        divCnt += 1

                newGraph[0][i][j] -= newGraph[1][i][j] * divCnt

    for a in range(1, clearUp[0]):
        for b in range(1, c - 1):
            newGraph[1][a][b] = newGraph[0][a][b]

    for a in range(clearDown[0] + 1, r - 1):
        for b in range(1, c - 1):
            newGraph[1][a][b] = newGraph[0][a][b]

    for i in range(2, c):
        newGraph[1][clearUp[0]][i] = newGraph[0][clearUp[0]][i - 1]

    for i in range(clearUp[0]):
        newGraph[1][i][c - 1] = newGraph[0][i + 1][c - 1]

    for i in range(c - 1):
        newGraph[1][0][i] = newGraph[0][0][i + 1]

    for i in range(1, clearUp[0]):
        newGraph[1][i][0] = newGraph[0][i - 1][0]

    for i in range(2, c):
        newGraph[1][clearDown[0]][i] = newGraph[0][clearDown[0]][i - 1]

    for i in range(clearDown[0] + 1, r - 1):
        newGraph[1][i][0] = newGraph[0][i + 1][0]

    for i in range(c - 1):
        newGraph[1][r - 1][i] = newGraph[0][r - 1][i + 1]

    for i in range(clearDown[0] + 1, r):
        newGraph[1][i][c - 1] = newGraph[0][i - 1][c - 1]

    newGraph[1][clearUp[0]][0] = -1
    newGraph[1][clearDown[0]][0] = -1

    newGraph[1][clearUp[0]][1] = 0
    newGraph[1][clearDown[0]][1] = 0

    newGraph[0] = deepcopy(newGraph[1])
    for i in range(r):
        for j in range(c):
            newGraph[1][i][j] = 0

total = 0
for i in range(r):
    for j in range(c):
        if newGraph[0][i][j] != -1:
            total += newGraph[0][i][j]

print(total)
