# 부분 삼각 수열 -> 정렬
from itertools import combinations
import sys

input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
print(a)
if len(a) < 3:
    length = len(a)
else:
    length = 1
    for i in range(len(a) - 2):
        for k in range(i + 2, len(a)):
            if a[i] + a[i + 1] > a[k]:
                length = max(length, (k - i) + 1)
            else:
                break
    if length == 1:
        length = 2
print(length)
