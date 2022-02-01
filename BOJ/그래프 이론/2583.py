# 영역 구하기

import sys
sys.setrecursionlimit(50000)
m, n, k = map(int, input().split())   # m : 5, n : 7
lst = [[0] * n for _ in range(m)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

# 직사각형 영역 방문처리
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(-(y2-m), -(y1-m)):
        for j in range(x1, x2):
            lst[i][j] = 1   # 직사각형의 영역에 대해 방문처리

cnt = []   # 각 영역 개수 체크 리스트
h = 0   # 구역 당 영역 넓이 체크

def dfs(x, y):
    global h
   
    if 0 <= x < m and 0 <= y < n:
        if lst[x][y] == 0:
            h += 1   # 구하는 영역 넓이 +
            lst[x][y] = 1   # 빙문 처리

            for i in range(len(dx)):
                nx = x + dx[i]
                ny = y + dy[i]
        
                dfs(nx, ny) 
                # return True   # 왜 이게 문제지..?

for i in range(m):
    for j in range(n):
        if lst[i][j] == 0:
            h = 0
            dfs(i, j)
            cnt.append(h)
 
print(len(cnt))
for i in sorted(cnt): print(i, end = ' ')