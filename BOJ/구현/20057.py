# 마법사 상어와 토네이도
import sys

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

sandX = [
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    [1, 1, 0, 0, -2, 0, 0, -1, -1],
]
sandY = [
    [1, 1, 0, 0, -2, 0, 0, -1, -1],
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
    [-1, -1, 0, 0, 2, 0, 0, 1, 1],
    [-1, 1, -2, 2, 0, -1, 1, -1, 1],
]

rate = [1, 1, 2, 2, 5, 7, 7, 10, 10]

dax = [0, 1, 0, -1]
day = [-1, 0, 1, 0]
startX, startY = int(n / 2), int(n / 2)


def sand(x, y, direction):
    tmp_out_val = 0
    curr_sand_val = graph[x][y]
    tmp_sum_sand_val = 0

    for i in range(len(sandX[direction])):
        windX = x + sandX[direction][i]
        windY = y + sandY[direction][i]
        tmp_sand_val = (curr_sand_val * rate[i]) // 100
        tmp_sum_sand_val += tmp_sand_val

        if 0 <= windX < n and 0 <= windY < n:
            graph[windX][windY] += tmp_sand_val
        else:
            tmp_out_val += tmp_sand_val

    tmp_sand_a = curr_sand_val - tmp_sum_sand_val
    wind_ax = x + dx[direction]
    wind_ay = y + dy[direction]

    if 0 <= wind_ax < n and 0 <= wind_ay < n:
        graph[wind_ax][wind_ay] += tmp_sand_a
    else:
        tmp_out_val += tmp_sand_a

    graph[x][y] = 0

    return tmp_out_val


def rotate_cycle():
    total_out = 0
    direction = moveCnt = 0
    dist = 1

    x, y = startX, startY
    while True:
        moveCnt += 1

        for _ in range(dist):
            nx = x + dx[direction]
            ny = y + dy[direction]
            if (nx, ny) == (0, -1):
                return total_out

            tmp_out_val = sand(nx, ny, direction)
            total_out += tmp_out_val

            x = nx
            y = ny

        if moveCnt == 2:
            dist += 1
            moveCnt = 0

        direction = (direction + 1) % 4


ans = rotate_cycle()
print(ans)
