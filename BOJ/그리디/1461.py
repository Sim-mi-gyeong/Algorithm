# 도서관

import heapq

n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

n, p = [], []
nList, pList = [], []

for i in lst:
    if i < 0:
        heapq.heappush(n, i)
    else:
        heapq.heappush(p, -i)

while n:
    if len(n) > 0:
        # 한 번에 이동할 각 위치 중 가장 큰 값의 값을 힙에서 꺼내고
        nList.append(abs(heapq.heappop(n)))
    # 한 번에 이동할 각 위치 중 가장 큰 값이 아닌(그보다 작은) 값들을 힙에서 꺼내기 -> 한 번에 책을 옮길 때 이동하게 될 각 위치
    for _ in range(m - 1):
        if n:
            heapq.heappop(n)

while p:
    if len(p) > 0:
        pList.append(-heapq.heappop(p))
    for _ in range(m - 1):
        if p:
            heapq.heappop(p)

if nList and pList:
    maxVal = max(max(nList), max(pList))
elif nList and not pList:
    maxVal = max(nList)
else:
    maxVal = max(pList)

dist = 2 * (sum(nList) + sum(pList)) - maxVal

print(dist)
