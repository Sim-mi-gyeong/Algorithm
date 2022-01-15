# 나이트의 이동
from collections import deque
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [-2, -1, 1, 2, 2, 1, -1, -2]
n = int(input())
queue = deque([])

def bfs(w, x, y, tx, ty):
    queue.append([x,y])   # 처음 위치
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < w and 0 <= ny < w:
                if path[nx][ny] == 0:   # 먼저 큐에 넣고 방문 처리
                    queue.append([nx, ny])
                    path[nx][ny] = path[x][y] + 1
                    if nx == tx and ny == ty:
                        print(path[nx][ny])
                        break 

for i in range(n):
    w = int(input())   # 한 변의 길이
    path = [[0] * w for _ in range(w)]
    x, y = map(int, input().split())   # 현재 위치
    tx, ty = map(int, input().split())   # 목표 위치 -> 까지 최소 몇 번만에?
    if x == tx and y == ty:
        print(0)
        continue
    bfs(w, x, y, tx, ty)