# 일루미네이션
from collections import deque

w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

# 짝수 줄 탐색 방향
dx1 = [-1, -1, 0, 1, 1, 0]
dy1 = [-1, 0, 1, 0, -1, -1]
# 홀수 줄 탐색 방향
dx2 = [-1, -1, 0, 1, 1, 0]
dy2 = [0, 1, 1, 1, 0, -1]

dx = [dx1, dx1]
dy = [dy1, dy2]
visited = [[0] * w for _ in range(h)]


def bfs(startX, startY):
    q = deque()
    q.append((startX, startY))
    visited[startX][startY] = 1
    cnt = 0

    while q:
        x, y = q.popleft()
        idx = (x + 1) % 2
        for i in range(6):
            nx = x + dx[idx][i]
            ny = y + dy[idx][i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                if graph[nx][ny] == 1:
                    cnt += 1
                elif graph[nx][ny] == 0:
                    q.append((nx, ny))
                    visited[nx][ny] = 1

    return cnt


totalCnt = 0
for i in [0, h - 1]:
    for j in range(w):
        if graph[i][j] == 1:
            totalCnt += 2
            if (i == 0 and j == w - 1) or (i == h - 1 and j == 0):
                totalCnt -= 1
        elif graph[i][j] == 0 and not visited[i][j]:
            totalCnt += bfs(i, j)

for i in range(h):
    for j in [0, w - 1]:
        if graph[i][j] == 1:
            if ((i + 1) % 2 == 1 and j == w - 1) or ((i + 1) % 2 == 0 and j == 0):
                totalCnt += 3
            elif ((i + 1) % 2 == 1 and j == 0) or ((i + 1) % 2 == 0 and j == w - 1):
                totalCnt += 1
        elif graph[i][j] == 0 and not visited[i][j]:
            totalCnt += bfs(i, j)

print(totalCnt)
