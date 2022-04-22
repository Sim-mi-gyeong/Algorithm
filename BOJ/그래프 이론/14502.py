# 연구소

from collections import deque
import sys
import copy

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def wall(cnt):
    global wallCnt
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                wall(cnt + 1)
                graph[i][j] = 0


maxSize = 0


def bfs():
    global maxSize
    copyGraph = copy.deepcopy(graph)

    queue = deque()

    for i in range(n):
        for j in range(m):
            if copyGraph[i][j] == 2:
                # visited[i][j] = 1  # 방문처리 -> 이걸 빼야 하는게, 위에서 wall 함수에서는 백트래킹 시 visited 도 이전 값으로 돌렸는데, bfs 에서는 이전으로 visited 상태를 돌리는 부분이 없었음
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if copyGraph[nx][ny] == 0:
                    copyGraph[nx][ny] = 2
                    queue.append((nx, ny))

    safeSize = 0
    for i in range(n):
        safeSize += copyGraph[i].count(0)
    maxSize = max(maxSize, safeSize)


wall(0)
print(maxSize)
