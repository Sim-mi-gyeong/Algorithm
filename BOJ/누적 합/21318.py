# 피아노 체조

import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
cntSum = [0] * n
for i in range(n - 1, 0, -1):
    if lst[i] < lst[i - 1]:
        # cntSum[i - 1] += 1
        cntSum[i - 1] = cntSum[i] + 1
    else:
        cntSum[i - 1] = cntSum[i]
print("cntSum : ", cntSum)

q = int(input())


def solve(start, end):
    return cntSum[start] - cntSum[end]


for _ in range(q):
    start, end = map(int, input().split())
    print(solve(start - 1, end - 1))
