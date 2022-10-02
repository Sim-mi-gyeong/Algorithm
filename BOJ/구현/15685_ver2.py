# 드래곤 커브

n = int(input())
graph = [[0] * 101 for _ in range(101)]
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


for _ in range(n):
    y, x, d, g = map(int, input().split())

    direction = [d]  # 이동 방향
    tmpDir = [d]  # 이동 방향을 만들기 위해 이전 세대에서 전달받은 방향 목록
    graph[x][y] = 1
    for _ in range(g + 1):
        for d in direction:  # 추가적으로 이동해야 하는 방향 좌표
            x += dx[d]
            y += dy[d]
            graph[x][y] = 1
        direction = [(tmpDir[i] + 1) % 4 for i in range(len(tmpDir))]  # (0 ->) 1 -> 1, 2 -> 1 2 3 2

        direction.reverse()  # 1 -> 2, 1 -> 2 3 2 1
        tmpDir = tmpDir + direction  # 0 1 -> 0, 1, 2, 1 -> 0 1 2 1 2 3 2 1

cnt = 0
for i in range(100):
    for j in range(100):
        if (
            graph[i][j] == 1
            and graph[i][j + 1] == 1
            and graph[i + 1][j] == 1
            and graph[i + 1][j + 1] == 1
        ):
            cnt += 1

print(cnt)
