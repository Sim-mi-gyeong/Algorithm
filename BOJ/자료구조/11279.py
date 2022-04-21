# 최대 힙

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
    if x > 0:  # x 추가
        heapq.heappush(q, -x)
    elif x == 0:  # 가장 큰 값 출력 -> 배열에서 제거
        print(-1 * (heapq.heappop(q)))
