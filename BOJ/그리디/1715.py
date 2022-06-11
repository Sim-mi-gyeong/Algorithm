# 카드 정렬하기

import heapq

n = int(input())
q = []
for _ in range(n):
    heapq.heappush(q, int(input()))

ans = 0
while len(q) > 1:
    tmp1 = heapq.heappop(q)
    tmp2 = heapq.heappop(q)
    ans += tmp1 + tmp2
    heapq.heappush(q, (tmp1 + tmp2))

print(ans)
