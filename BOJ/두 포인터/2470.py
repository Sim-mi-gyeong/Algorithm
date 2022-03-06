# 두 용액
# 시간 초과 -> 이분탐색으로 풀기

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
sumValue = 0
INF = int(1e9)
minD = INF
for start in range(n-1):
    sumValue = lst[start]
    for end in range(start + 1, n):
        sumValue += lst[end]
        d = abs(sumValue - 0)
        sumValue -= lst[end]
        if minD > d:
            minD = d
            s, e = lst[start], lst[end]

print(s, e)