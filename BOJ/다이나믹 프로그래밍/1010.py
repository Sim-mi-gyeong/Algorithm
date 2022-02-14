# 다리 놓기

import itertools
import math
t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    cnt = 1
    for i in range(m, m-n, -1): cnt *= i
    for j in range(1, n+1): cnt //= j
    print(cnt)

# for i in range(t):
#     n, m = map(int, input().split())
#     nCr = itertools.combinations(range(m), n)
#     print(len(list(nCr)))  