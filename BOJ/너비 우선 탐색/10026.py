# 적록색약

from array import array
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

        for i in range(len(dx)):   # 꺼낸 뒤 상하좌우 위치 탐색! 
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:   # 이탈 여부 확인 
                # bfs 수행 시기마다 각 종류의 색깔 정보에 대해 탐색 -> bfs 한 번 호출마다 한 개의 색깔 일치 여부 탐색 
                if array[nx][ny] == c: # bfs 를 수행하고자 하는 위치의 색깔 & 방문하지 않은 경우
                    array[nx][ny] = 1   # 방문 처리
                    queue.append([nx, ny])   # 방문 처리가 완료된 위치에 대해 큐에 넣기
        
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
            bfs(i, j, gridY[i][j], gridY)   # 위치 정보와 색깔에 대한 정보가 포함되어야 함.
            cnt0 += 1
        
# 색맹이 아닌 경우 bfs 수행
for i in range(n):
    for j in range(n):
        if grid[i][j] != 1:
            bfs(i, j, grid[i][j], grid)
            cnt1 += 1
print(cnt1, cnt0)
print(grid)