# 주사위 굴리기

n, m, x, y, k = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
dir = list(map(int, input().split()))
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
rec = [0, 0, 0, 0, 0, 0, 0]


def rotation(direct):
    if direct == 1:
        rec[1], rec[3], rec[6], rec[4] = rec[4], rec[1], rec[3], rec[6]
    elif direct == 2:
        rec[1], rec[4], rec[6], rec[3] = rec[3], rec[1], rec[4], rec[6]
    elif direct == 3:
        rec[1], rec[2], rec[6], rec[5] = rec[5], rec[1], rec[2], rec[6]
    else:
        rec[1], rec[5], rec[6], rec[2] = rec[2], rec[1], rec[5], rec[6]


for i in dir:
    nx = x + dx[i - 1]
    ny = y + dy[i - 1]

    if 0 <= nx < n and 0 <= ny < m:
        rotation(i)
        if graph[nx][ny] == 0:
            graph[nx][ny] = rec[6]
        else:
            rec[6] = graph[nx][ny]
            graph[nx][ny] = 0
        x, y = nx, ny
    else:
        continue

    print(rec[1])
