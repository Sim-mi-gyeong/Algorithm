# 어른 상어
import sys

input = sys.stdin.readline
dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]
n, m, k = map(int, input().split())
graph = []
shark = []
shark_loc_dic = dict()
info_graph = [[[0] * 2 for _ in range(n)] for _ in range(n)]


def init_smell(sharkX, sharkY, sharkNum):
    global info_graph
    info_graph[sharkX][sharkY][0] = sharkNum
    info_graph[sharkX][sharkY][1] = k


for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(n):
        if tmp[j] != 0:
            graph[i][j] = tmp[j]
            shark.append(tmp[j])
            init_smell(i, j, tmp[j])
            shark_loc_dic[tmp[j]] = (i, j)

dir_input = list(map(int, input().split()))
shark_dir_dic = dict()
for i in range(1, m + 1):
    shark_dir_dic[i] = dir_input[i - 1]

sharkDir = []
for _ in range(m):
    totalDir = []
    for i in range(4):
        tmp = list(map(int, input().split()))
        totalDir.append(tmp)
    sharkDir.append(totalDir)


def move_shark():
    global shark_dir_dic, shark_loc_dic, shark, k, graph, info_graph
    for i in range(1, m + 1):
        check = False
        if i not in shark:
            continue
        currX, currY = shark_loc_dic[i][0], shark_loc_dic[i][1]
        currDir = shark_dir_dic[i]
        for j in range(4):
            nextDir = sharkDir[i - 1][currDir - 1][j]
            nx = currX + dx[nextDir]
            ny = currY + dy[nextDir]
            if 0 <= nx < n and 0 <= ny < n:
                if info_graph[nx][ny][0] == 0:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = i
                        graph[currX][currY] = 0
                        shark_loc_dic[i] = (nx, ny)
                        shark_dir_dic[i] = nextDir
                    else:
                        graph[currX][currY] = 0
                        shark.remove(i)
                    check = True
                    break

        if check:
            continue

        for j in range(4):
            nextDir = sharkDir[i - 1][currDir - 1][j]
            nx = currX + dx[nextDir]
            ny = currY + dy[nextDir]
            if 0 <= nx < n and 0 <= ny < n:
                if info_graph[nx][ny][0] == i:
                    graph[nx][ny] = i
                    graph[currX][currY] = 0
                    shark_loc_dic[i] = (nx, ny)
                    shark_dir_dic[i] = nextDir
                    break


def update_smell():
    global info_graph
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                info_graph[i][j][0] = graph[i][j]
                info_graph[i][j][1] = k
            else:
                if info_graph[i][j][1] == 1:
                    info_graph[i][j][0] = 0
                    info_graph[i][j][1] = 0
                elif info_graph[i][j][1] >= 1:
                    info_graph[i][j][1] -= 1


def chek_shark_exist():
    if len(shark) == 1 and shark[0] == 1:
        return True
    return False


time = 0
check = True
while True:
    if chek_shark_exist():
        break

    if time >= 1000:
        check = False
        break

    move_shark()
    update_smell()
    time += 1

if check:
    print(time)
else:
    print(-1)
