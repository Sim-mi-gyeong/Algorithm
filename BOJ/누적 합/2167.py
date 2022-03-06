# 2차원 배열의 합

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
k = int(input())

for _ in range(k):
    i, j, x, y = map(int, input().split())   # 1 부터 시작
    ans = 0
    for a in range(i-1, x-1+1):
        for b in range(j-1, y-1+1):
            ans += lst[a][b]

    print(ans)