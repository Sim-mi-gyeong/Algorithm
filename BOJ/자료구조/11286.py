# 절댓값 힙

import heapq
import sys

input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if len(q) == 0 and x == 0:
        print(0)
        continue
    if x > 0:
        heapq.heappush(q, (x, x))
    elif x < 0:
        heapq.heappush(q, (-x, x))
    else:
        popValue = heapq.heappop(q)
        print(popValue[1])
