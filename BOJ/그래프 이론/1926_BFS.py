# 그림
# 런타임 에러(1 1 / 0) -> 예외 처리 !!
from collections import deque

n, m = map(int, input().split())
pic = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

lst = []   # 그림 종류를 담을 list

def bfs(x, y):
    cnt = 0
    queue = deque([])
    visited[x][y] = 1
    queue.append([x, y])
    cnt += 1
   
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if pic[nx][ny] == 1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    cnt += 1
                    queue.append([nx, ny])
                else:
                    continue
    return cnt

# len, max = 0, 0 으로 먼저 선언 -> max 업데이트 및 예외처리 가능
for i in range(n):
    for j in range(m):
        if pic[i][j] == 1 and visited[i][j] == 0: 
            ans = bfs(i, j)
            if ans != 0: lst.append(ans)  

if len(lst) != 0: 
    print(len(lst))
    print(max(lst))
else:
    print(len(lst))
    print(0)