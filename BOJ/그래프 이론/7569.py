# 토마토
from collections import deque
# 위 아래 앞 뒤 왼쪽 오른쪽
dx = [-1, 1, 0, 0, 0, 0 ]   # 층
dy = [0, 0, -1, 1, 0, 0]   # 행
dz = [0, 0, 0, 0, -1, 1]   # 열
ans = 0
m, n, h = map(int, input().split())   # 열, 행, 층

tomato = []
for i in range(h):
    tmp = [list(map(int, input().split())) for _ in range(n)]
    tomato.append(tmp)

queue = deque([])
for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 1: 
                queue.append([k, i, j])

def bfs():  
   while queue:
       x, y, z = queue.popleft()

       for i in range(len(dx)):
           nx = x + dx[i]
           ny = y + dy[i]
           nz = z + dz[i]

           if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m:
               if tomato[nx][ny][nz] == -1: pass
               if tomato[nx][ny][nz] == 0:
                   tomato[nx][ny][nz] = tomato[x][y][z] + 1
                   queue.append([nx, ny, nz])
bfs()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if tomato[k][i][j] == 0:
                print(-1)
                exit(0)            
        ans = max(ans, max(tomato[k][i]))
print(ans - 1)