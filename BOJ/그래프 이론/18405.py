# 경쟁적 전염

import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
virus = []  # 처음 각 바이러스는 여러 개 존재 가능 -> 딕셔너리 사용 시 한 종류의 바이러스에 대해 한 개의 위치만 저장
graph = []
for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], i, j, 0))

s, targetX, targetY = map(int, input().split())
virus = sorted(virus, key=lambda x: x[0])
q = deque(virus)

while q:
    num, x, y, time = q.popleft()
    if time == s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = num
                q.append((num, nx, ny, time + 1))

print(graph[targetX - 1][targetY - 1])
