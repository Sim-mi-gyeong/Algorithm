# 달팽이

n = int(input())
target = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = [[0] * n for _ in range(n)]
tartgetX, targetY = n // 2 + 1, n // 2 + 1  # 초기화 -> target 기준 초기화 조건 설정


def snail():
    global tartgetX, targetY

    move_cnt = dir = 0
    dist = num = 1
    x, y = n // 2, n // 2
    graph[x][y] = num

    while True:
        move_cnt += 1

        for _ in range(dist):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if (nx, ny) == (-1, 0):
                return

            num += 1
            if num == target:
                tartgetX, targetY = nx + 1, ny + 1
            graph[nx][ny] = num

            x, y = nx, ny

        if move_cnt == 2:
            dist += 1
            move_cnt = 0

        dir = (dir + 1) % 4


snail()
for i in range(len(graph)):
    print(*graph[i])
print(tartgetX, targetY)
