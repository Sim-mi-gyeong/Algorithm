# 새로운 게임

import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

graph = []
for i in range(n):
    tmp = list(map(int, input().rstrip().split()))
    graph.append(tmp)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
horse = dict()
graph_info = [[[] for _ in range(n)] for _ in range(n)]

for i in range(1, k + 1):
    r, c, d = map(int, input().rstrip().split())
    r -= 1
    c -= 1
    d -= 1
    horse[i] = [r, c, d]
    graph_info[r][c].append(i)

def checkUnder(horseNum, x, y, dir):
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
    changeDirFlag = False

    if not (0 <= nx < n and 0 <= ny < n):
        newDir = changeDir(dir)
        horse[horseNum][2] = newDir
        nx = x + dx[newDir]
        ny = y + dy[newDir]
        changeDirFlag = True

    if graph[nx][ny] == 0:
        tmpNum = len(graph_info[x][y])
        for i in range(tmpNum):
            graph_info[nx][ny].append(graph_info[x][y][i])
        graph_info[x][y] = []

    elif graph[nx][ny] == 1:
        tmpNum = len(graph_info[x][y])
        for i in range(tmpNum):
            graph_info[nx][ny].append(graph_info[x][y][i])
        graph_info[x][y] = []

        graph_info[nx][ny] = graph_info[nx][ny][::-1]

    elif graph[nx][ny] == 2:
        if changeDirFlag:
            nx = x
            ny = y
        else:
            newDir = changeDir(dir)
            horse[horseNum][2] = newDir
            nx = x + dx[newDir]
            ny = y + dy[newDir]

            if not (0 <= nx < n and 0 <= ny < n):
                nx = x
                ny = y
            else:
                if graph[nx][ny] == 0:
                    tmpNum = len(graph_info[x][y])
                    for i in range(tmpNum):
                        graph_info[nx][ny].append(graph_info[x][y][i])
                    graph_info[x][y] = []
         
                elif graph[nx][ny] == 1:
                    tmpNum = len(graph_info[x][y])
                    for i in range(tmpNum):
                        graph_info[nx][ny].append(graph_info[x][y][i])
                    graph_info[x][y] = []
         
                    graph_info[nx][ny] = graph_info[nx][ny][::-1]
                    
                elif graph[nx][ny] == 
                    nx, ny = x, y
  
    horse[horseNum][0] = nx
    horse[horseNum][1] = ny

    for tmpHorse in graph_info[nx][ny]:
        horse[tmpHorse][0] = nx
        horse[tmpHorse][1] = ny

    if checkEnd():
        return 1

def solve():
    for horseNum, horseInfo in horse.items():
        x, y, dir = horseInfo[0], horseInfo[1], horseInfo[2]
        if checkUnder(horseNum, x, y, dir):
            if move(horseNum, x, y, dir):
                return 1


def checkEnd():
    flag = False
    for i in range(n):
        for j in range(n):
            if len(graph_info[i][j]) >= 4:
                flag = True
    return flag


turn = 0
while True:
    turn += 1
    if solve():
        print(turn)
        break

    if checkEnd():
        print(turn)
        break

    if turn > 10:
        print(-1)
        break
