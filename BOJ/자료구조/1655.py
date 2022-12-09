# 가운데를 말해요

import heapq
import sys

n = int(sys.stdin.readline())
leftHeap, rightHeap = [], []  # max heap, min heap

"""
for _ in range(n):
    a = int(input())
    if len(leftHeap) == len(rightHeap):   # 지금까지, 짝수 개를 불렀으면
        heapq.heappush(leftHeap, (-a, a))
    else:
        heapq.heappush(rightHeap, (a, a))
    # Min Heap(right heap) 의 가장 작은 값보다 < Max Heap(left heap)의 가장 큰 값이 더 크면 값을 바꿔
    if rightHeap and leftHeap[0][1] > rightHeap[0][1]:
        leftValue = heapq.heappop(leftHeap)[1]
        rightValue = heapq.heappop(rightHeap)[1]
        heapq.heappush(rightHeap, (leftValue, leftValue))   # 최소 힙
        heapq.heappush(leftHeap, (-rightValue, rightHeap))   # 최대 힙

    print(leftHeap[0][1])

print('leftHeap : ', leftHeap)
"""


for _ in range(n):
    num = int(sys.stdin.readline())

    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)
    else:
        heapq.heappush(rightHeap, num)

    if rightHeap and rightHeap[0] < -leftHeap[0]:
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)
        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0])
