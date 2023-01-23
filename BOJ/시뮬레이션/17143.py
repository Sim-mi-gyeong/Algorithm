# 낚시왕

import sys

input = sys.stdin.readline

h, w, m = map(int, input().rstrip().split())
graph = [[0] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        graph[i][j] = []

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

shark_dic = dict()
for sharkNum in range(1, m + 1):
    r, c, s, d, z = map(int, input().rstrip().split())
    x = r - 1
    y = c - 1
    d -= 1

    graph[x][y].append(sharkNum)
    shark_dic[sharkNum] = [x, y, s, d, z]

startX, startY = -1, 0

cnt = 0


def catch(x):
    global cnt

    shark_list = []
    for i in range(h):
        if len(graph[i][x]) != 0:
            sharkNum = graph[i][x][0]
            size = shark_dic[sharkNum][4]
            shark_list.append((sharkNum, i, x, size))

    if len(shark_list) == 0:
        return

    shark_list = sorted(shark_list, key=lambda x: x[1])

    catch_shark = shark_list[0]
    catch_shark_num, catch_shark_x, catch_shark_y, catch_shark_size = (
        catch_shark[0],
        catch_shark[1],
        catch_shark[2],
        catch_shark[3],
    )

    cnt += catch_shark_size

    graph[catch_shark_x][catch_shark_y] = []
    del shark_dic[catch_shark_num]


def move():
    new_graph = [[[] for _ in range(w)] for _ in range(h)]
    for sharkNum, sharkInfo in shark_dic.items():
        x, y = sharkInfo[0], sharkInfo[1]
        # graph[x][y] = []
        s, d, z = sharkInfo[2], sharkInfo[3], sharkInfo[4]
        if s == 0:
            nx, ny = x, y
        else:
            for _ in range(s):
                if not (0 <= x + dx[d] < h and 0 <= y + dy[d] < w):
                    if d == 0:
                        d = 1
                    elif d == 1:
                        d = 0
                    elif d == 2:
                        d = 3
                    elif d == 3:
                        d = 2
                nx = x + dx[d]
                ny = y + dy[d]

                x, y = nx, ny

        new_graph[nx][ny].append(sharkNum)

        shark_dic[sharkNum][0] = nx
        shark_dic[sharkNum][1] = ny
        shark_dic[sharkNum][3] = d

    for i in range(h):
        for j in range(w):
            graph[i][j] = new_graph[i][j]

    for i in range(h):
        for j in range(w):
            if len(graph[i][j]) >= 2:
                maxSize = 0
                maxSharkNum = 0
                for sharkNum in graph[i][j]:
                    sharkSize = shark_dic[sharkNum][4]
                    if maxSize < sharkSize:
                        maxSize = sharkSize
                        maxSharkNum = sharkNum

                for sharkNum in graph[i][j]:
                    if sharkNum != maxSharkNum:
                        del shark_dic[sharkNum]

                graph[i][j] = [maxSharkNum]


while True:
    startX += 1

    catch(startX)
    move()

    if startX == w - 1:
        break
    if len(shark_dic) == 0:
        break


print(cnt)

