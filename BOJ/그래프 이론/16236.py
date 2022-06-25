# 아기 상어

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]
sharkSize = 2
eatCnt = 0
time = 0
# 먹은 물고기에 대해 방문처리 -> s는 0으로


def bfs(x, y):
    global sharkSize, eatCnt, time
    queue = deque([])
    if not visited[x][y]:
        visited[x][y] = True
        queue.append([x, y])

    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                time += 1
                if sharkSize > s[nx][ny]:  # 물고기를 먹을 수 있을 때
                    eatCnt += 1
                    visited[nx][ny] = True
                    s[x][y] = 0
                    queue.append([nx, ny])

                    if eatCnt == sharkSize:
                        sharkSize += 1
                        eatCnt = 0

                elif sharkSize == s[nx][ny]:  # 먹지는 못하고, 이동만 가능
                    queue.append([nx, ny])

                elif s[nx][ny] == 0:
                    queue.append([nx, ny])

    # 더이상 먹을 수 있는 물고기가 없을 때,
    for i in range(n):
        for j in range(n):
            if s[i][j] != 0 or s[i][j] != 9:
                return eatCnt


for i in range(n):
    for j in range(n):
        if s[i][j] == 9:
            x, y = i, j
print(bfs(x, y))
