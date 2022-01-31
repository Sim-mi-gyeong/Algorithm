# 적록색약

from collections import deque

n = int(input())
grid = [list(list(input())) for _ in range(n)]
gridY = [[0] * n for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
queue = deque([])
cnt0, cnt1 = 0, 0

def bfs(x, y, c, array):
    queue.append([x, y])
    array[x][y] = 1    # 방문 처리
    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if array[nx][ny] == c: # bfs 를 수행하고자 하는 위치의 색깔 & 방문하지 않은 경우
                    array[nx][ny] = 1   # 방문 처리
                    queue.append([nx, ny])

        
# 색맹인 경우(R == G)
for i in range(n):
    for j in range(n):
        if grid[i][j] == 'R' or grid[i][j] == 'G': 
            gridY[i][j] = 'R'
        else: gridY[i][j] = 'B'

# 색맹인 경우 bfs 수행
for i in range(n):
    for j in range(n):
        if gridY[i][j] != 1:   # 방문 처리 되지 않은 위치에 대해
            bfs(i, j, gridY[i][j], gridY)
            cnt0 += 1
        
# 색맹이 아닌 경우 bfs 수행
for i in range(n):
    for j in range(n):
        if grid[i][j] != 1:
            bfs(i, j, grid[i][j], grid)
            cnt1 += 1
print(cnt1, cnt0)