# 강의실 배정
import heapq

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst = sorted(lst, key=lambda x: x[0])

heap = []
firstStart, firstEnd = lst[0][0], lst[0][1]
heapq.heappush(heap, (firstEnd, firstStart))

for i in range(1, len(lst)):
    start, end = lst[i][0], lst[i][1]
    topEnd, topStart = heap[0][0], heap[0][1]
    if start < topEnd:
        heapq.heappush(heap, (end, start))
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, (end, start))

print(len(heap))

"""
5
1 7
2 3
3 4
4 8
7 10

answer : 2
"""
