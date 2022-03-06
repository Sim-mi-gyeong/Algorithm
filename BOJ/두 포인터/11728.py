# 배열 합치기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lstA = list(map(int, input().split()))
lstB = list(map(int, input().split()))
lstSum = lstA + lstB
lstSum.sort()
# for i in lstSum: print(i, end = ' ')
print(*lstSum)