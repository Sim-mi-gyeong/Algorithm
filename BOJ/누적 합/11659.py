# 구간 합 구하기 4

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))
tmpSum = 0
sumList = [0]
for i in range(n):
    tmpSum += lst[i]
    sumList.append(tmpSum)

for i in range(m):
    i, j = map(int, input().split())
    print(sumList[j] - sumList[i-1])