# 새로운 게임

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

graph = []
for _ in range(n):
    tmp = list(map(int, input().rstrip().split()))
    graph.append(tmp)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horse = dict()
graph_info = [[deque() for _ in range(n)] for _ in range(n)]

for i in range(1, k + 1):
    r, c, d = map(int, input().rstrip().split())
    r -= 1
    c -= 1
    d -= 1
    horse[i] = [r, c, d]
    graph_info[r][c].append(i)


def checkUnder(horseNum, x, y):
    flag = False
    if len(graph_info[x][y]) >= 1 and graph_info[x][y][0] == horseNum:
        flag = True
    return flag


def changeDir(dir):
    if dir == 0:
        dir = 1
    elif dir == 1:
        dir = 0
    elif dir == 2:
        dir = 3
    elif dir == 3:
        dir = 2

    return dir

def move(horseNum, x, y, dir):
    nx = x + dx[dir]
    ny = y + dy[dir]

    if not (0 <= nx < n and 0 <= ny < n) or graph[nx][ny] == 2:
        newDir = changeDir(dir)
        horse[horseNum][2] = newDir
        nx = x + dx[newDir]
        ny = y + dy[newDir]

        if not (0 <= nx < n and 0 <= ny < n) or graph[nx][ny] == 2:
            nx = x
            ny = y

        elif graph[nx][ny] == 0:
            while graph_info[x][y]:
                tmpHorseNum = graph_info[x][y].popleft()
                graph_info[nx][ny].append(tmpHorseNum)
                horse[tmpHorseNum][0] = nx
                horse[tmpHorseNum][1] = ny

        elif graph[nx][ny] == 1:
            while graph_info[x][y]:
                tmpHorseNum = graph_info[x][y].pop()
                graph_info[nx][ny].append(tmpHorseNum)
                horse[tmpHorseNum][0] = nx
                horse[tmpHorseNum][1] = ny

    elif graph[nx][ny] == 0:
        while graph_info[x][y]:
            tmpHorseNum = graph_info[x][y].popleft()
            graph_info[nx][ny].append(tmpHorseNum)
            horse[tmpHorseNum][0] = nx
            horse[tmpHorseNum][1] = ny

    elif graph[nx][ny] == 1:
        while graph_info[x][y]:
            tmpHorseNum = graph_info[x][y].pop()
            graph_info[nx][ny].append(tmpHorseNum)
            horse[tmpHorseNum][0] = nx
            horse[tmpHorseNum][1] = ny

    if len(graph_info[nx][ny]) >= 4:
        return 1


def solve():
    for horseNum, horseInfo in horse.items():
        x, y, dir = horseInfo[0], horseInfo[1], horseInfo[2]
        if checkUnder(horseNum, x, y):
            if move(horseNum, x, y, dir):
                return 1


turn = 0
while True:
    turn += 1
    if solve():
        print(turn)
        break

    if turn > 1000:
        print(-1)
        break

