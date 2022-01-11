# 유기농 배추
import sys
sys.setrecursionlimit(50000000)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
cnt = 0
t = int(input())

def dfs(x, y):
    if x < 0 or y < 0 or x >= m or y >= n:
        return False
    if ground[y][x] == 1:
        ground[y][x] = 0

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

for i in range(t):
    m, n, k = map(int, input().split())   # m: 가로(열), n: 세로(행)
    ground = list()
    for i in range(n):   
        tmp = []
        for j in range(m):
            tmp.append(0)
        ground.append(tmp)
    for i in range(k):
        x, y = map(int, input().split())   # x가 가로 위치(열), y가 세로 위치(행)
        ground[y][x] = 1

    for i in range(m):
        for j in range(n):
            if dfs(i, j): cnt += 1
    print(cnt)
    cnt = 0