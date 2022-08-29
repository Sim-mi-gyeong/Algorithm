# 음식물 피하기

from collections import deque

n, m, k = map(int, input().split())
graph = [["."] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    graph[r - 1][c - 1] = "#"

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0] * m for _ in range(n)]
maxVal = 0
cnt = 0


def bfs(graph, startX, startY):
    q = deque()
    global cnt
    visited[startX][startY] = 1
    q.append((startX, startY))
    cnt = 1

    while q:
        x, y = q.popleft()  # 큐에서 꺼낼 때 들고다니면, 나뉘는 부분에서는 그 수를 계속해서 누적해서 가져갈 수 없음

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == "#":
                    cnt += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    return cnt


for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j] == "#":
            maxVal = max(maxVal, bfs(graph, i, j))
print(maxVal)
