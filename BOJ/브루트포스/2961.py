# 도영이가 만든 맛있는 음식

from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())
num = [i + 1 for i in range(n)]
material = dict()
for i in range(1, n + 1):
    material[i] = list(map(int, input().split()))
ans = 1e9

for i in range(1, n + 1):
    kind = list(combinations(num, i))

    for j in range(len(kind)):
        totalS, totalB = 1, 0

        for k in range(len(kind[j])):
            lst = material[kind[j][k]]
            totalS *= lst[0]
            totalB += lst[1]

        d = abs(totalS - totalB)
        if ans >= d:
            ans = d
print(ans)
