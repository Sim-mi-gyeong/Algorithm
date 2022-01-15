# 안전영역 - BFS version
# 다시 

from collections import deque

n = int(input())
path = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
queue = deque([])
cnt = 0
def bfs():
    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]    
            if 0 <= nx < n and 0 <= ny < n:
                if land[nx][ny] == 0:
                    queue.append([nx, ny])
                    # 방문처리
                    land[nx][ny] = land[x][y] + 1

# 높이 범위 생성
ran = []
for i in range(n):
    for j in range(n):
        if path[i][j] not in ran:
            ran.append(path[i][j])
ran.sort()            

for h in ran:
    land = [[0] * n for _ in range(n)]
    # 제한 높이 설정
    for i in range(n):
        for j in range(n):
            # 제한 높이 보다 작거나 같은 경우
            if path[i][j] <= h:                
                land[i][j] = 1    # 방문 처리

    for i in range(n):
        for j in range(n):
            queue.append([i, j])
    
    bfs()

    for i in range(n):
        for j in range(n):
            cnt = max(cnt, max(land[i]))

print(cnt)