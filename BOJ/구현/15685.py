# 드래곤 커브

n = int(input())
graph = [[0] * 101 for _ in range(101)]
# 동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]


for _ in range(n):
    y, x, d, g = map(int, input().split())

    direction = [d]
    graph[x][y] = 1

    # g 번만큼 드래곤 커브 방향 추가
    for c in range(g):
        tmp = []
        for i in range(len(direction) - 1, -1, -1):
            # 이전 세대의 뒤에서부터 추가
            dir = (direction[i] + 1) % 4
            tmp.append(dir)
        direction = direction + tmp

    # 한 번에 이어붙이기
    for i in direction:
        x += dx[i]
        y += dy[i]
        graph[x][y] = 1

# 정사각형의 네 꼭짓점이 모두 -> 드래곤 커브의 일부인 경우의 수
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
