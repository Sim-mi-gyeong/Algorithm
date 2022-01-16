from collections import deque
dx = [-1, 0, 1]
dy = [1, 1, 1]
t = int(input())
# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
for i in range(t):
    n, m = map(int, input().split())   # n: 행, m: 열
    s = list(map(int, input().split()))

    ground = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(s[i * m + j])
        ground.append(tmp)
    start = ground[0][0]
    for i in range(n):
        start = max(start, ground[i][0])
    # for i in range(len(dx)):


    d = [[0] * (n * m)]
    
# def bfs():
#     queue = deque([])
#     while queue:
