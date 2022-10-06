# 빙산
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
snow = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(m):
        if tmp[j] != 0:
            snow.append((i, j))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(startX, startY):
    q = deque()
    visited[startX][startY] = 1
    q.append((startX, startY))
    meltList = deque()

    while q:
        x, y = q.popleft()
        seaCnt = 0
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] == 0:
                    seaCnt += 1
                elif graph[nx][ny] != 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

        if seaCnt > 0:
            meltList.append((x, y, seaCnt))

    while meltList:
        x, y, seaCnt = meltList.popleft()
        for _ in range(seaCnt):
            if graph[x][y] >= 1:
                graph[x][y] -= 1

    return 1  # 하나의 연결된 빙산 그룹 탐색


time = 0
check = False
while snow:
    groupCnt = 0
    visited = [[0] * m for _ in range(n)]
    meltList = []
    for i, j in snow:
        if graph[i][j] != 0 and not visited[i][j]:
            groupCnt += bfs(i, j)
        if graph[i][j] == 0:
            meltList.append((i, j))
    if groupCnt > 1:
        check = True
        break

    snow = sorted(list(set(snow) - set(meltList)))
    time += 1  # 입력 상태가 조건을 만족할 경우 시간 추가 전 결과 출력

if check:
    print(time)
else:
    print(0)
