# 달팽이
n = int(input())
target = int(input())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
graph = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]
tartgetX, targetY = n // 2 + 1, n // 2 + 1  # 초기화 -> target 기준 초기화 조건 설정


def snail():
    global tartgetX, targetY
    num = 1
    dir = -1

    x, y = n // 2, n // 2
    graph[x][y] = num
    visited[x][y] = 1
    while True:

        num += 1

        if (x, y) == (0, 0):
            break

        next_dir = (dir + 1) % 4
        nx = x + dx[next_dir]
        ny = y + dy[next_dir]

        if visited[nx][ny]:  # 이미 이동한 위치라면
            # 기존 방향으로 나아가기
            next_dir = dir
            nx = x + dx[next_dir]
            ny = y + dy[next_dir]

        graph[nx][ny] = num
        visited[nx][ny] = 1

        if num == target:
            tartgetX, targetY = nx + 1, ny + 1

        x, y, dir = nx, ny, next_dir


snail()
for i in range(len(graph)):
    print(*graph[i])
print(tartgetX, targetY)
