# 마법사 상어와 복제
import sys
import copy

input = sys.stdin.readline

fish_dx = [0, -1, -1, -1, 0, 1, 1, 1]
fish_dy = [-1, -1, 0, 1, 1, 1, 0, -1]
shark_dx = [-1, 0, 1, 0]
shark_dy = [0, -1, 0, 1]
m, s = map(int, input().rstrip().split())

n = 4
graphSmell = [[0] * n for _ in range(n)]
graph = [[[] for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, d = map(int, input().rstrip().split())
    graph[x - 1][y - 1].append(d - 1)

sharkX, sharkY = map(int, input().rstrip().split())
sharkX -= 1
sharkY -= 1


def check_move(targetX, targetY):
    check = True
    if not (0 <= targetX < n and 0 <= targetY < n):
        check = False
        return check

    if (targetX, targetY) == (sharkX, sharkY):
        check = False
        return check

    if graphSmell[targetX][targetY] != 0:
        check = False
        return check
    return check


def moveFish():
    global graph
    afterGraph = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(len(graph[i][j])):
                dir = graph[i][j][k]
                flag = False
                for _ in range(len(fish_dx)):
                    di = i + fish_dx[dir]
                    dj = j + fish_dy[dir]
                    if check_move(di, dj):
                        afterGraph[di][dj].append(dir)
                        flag = True
                        break
                    dir = (dir + 7) % 8

                if not flag:
                    afterGraph[i][j].append(dir)

    graph = afterGraph


def dfs(x, y, cnt, tmpFishCnt, visited):
    global maxFishCnt, sharkX, sharkY, bestDir
    if cnt == 3:
        if maxFishCnt < tmpFishCnt:
            maxFishCnt = tmpFishCnt
            sharkX, sharkY = x, y
            # bestDir = copy.deepcopy(visited)
            bestDir = visited[:]
        return

    for i in range(len(shark_dx)):
        nx = x + shark_dx[i]
        ny = y + shark_dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if (nx, ny) not in visited:
                visited.append((nx, ny))
                dfs(nx, ny, cnt + 1, tmpFishCnt + len(graph[nx][ny]), visited)
                visited.pop()
            else:
                dfs(nx, ny, cnt + 1, tmpFishCnt, visited)


for _ in range(s):
    maxFishCnt = -1
    bestDir = list()
    copyGraph = copy.deepcopy(graph)

    moveFish()

    dfs(sharkX, sharkY, 0, 0, list())

    for x, y in bestDir:
        if len(graph[x][y]) > 0:
            graph[x][y] = []
            graphSmell[x][y] = 3

    for i in range(n):
        for j in range(n):
            if graphSmell[i][j]:
                graphSmell[i][j] -= 1

    for i in range(n):
        for j in range(n):
            graph[i][j] += copyGraph[i][j]

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(graph[i][j])

print(ans)
