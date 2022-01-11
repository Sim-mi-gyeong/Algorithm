# 토마토
# 최소 일수, 주변의 토마토들을 익힘 
# BFS로 -> 최단 거리를 구하는 문제와 동일
from collections import deque

m, n = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
cnt = 0
queue = deque([])

for i in range(n):
  for j in range(m):
    if land[i][j] == 1:
        queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()   # 원소가 2개인 리스트를 pop 해서 각 원소 변수 지정
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if land[x][y] == -1:
                    pass
                if land[nx][ny] == 0:   # 먼저 큐에 넣고 방문 처리
                    queue.append([nx, ny])
                    land[nx][ny] = land[x][y] + 1

bfs()
for i in range(n):
    for j in range(m):
        if land[i][j] == 0: 
            print(-1)
            exit(0)   # 바로 강제 프로세스 종료 / 함수 속에서 return -> 그 함수만 종료
    cnt = max(cnt, max(land[i]))
print(cnt - 1)