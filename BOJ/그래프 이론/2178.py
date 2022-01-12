# 미로 탐색
# 최단 경로 -> BFS(방문 처리를 이전 위치 + 1 처리)
from collections import deque
n, m = map(int, input().split())
path = [list(map(int, input())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque([])
queue.append([0, 0])

def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx, ny = x + dx[i], y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                # 최단 거리에 대해서는, 이미 가장 빠른 경로로 나가는 경우에 대해 path[nx][ny]의 값이 + 되기 때문에 따로 처리 X
                if path[nx][ny] == 1:  
                    path[nx][ny] = path[x][y] + 1
                    queue.append([nx, ny])
bfs()
print(path[n-1][m-1])