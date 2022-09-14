# 이중 우선순위 큐
# 힙에 넣을 때마다 힙 정렬 수행


import heapq
import sys

input = sys.stdin.readline


def heapify(arr, index, size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < size and arr[left] > arr[largest]:
        largest = left
    if right < size and arr[right] > arr[largest]:
        largest = right
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, size)


def heapSort(arr):
    n = len(arr)
    for i in range(n // 2, -1, -1):
        heapify(arr, i, n)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

    return arr


t = int(input())
for _ in range(t):
    k = int(input())
    q = []
    for _ in range(k):
        cal, num = input().split()
        num = int(num)
        if cal == "D" and len(q) == 0:
            continue
        elif cal == "I":
            heapq.heappush(q, num)
            q = heapSort(q)

        elif cal == "D":
            if num == 1:
                print(q.pop(-1))
            else:
                print(q.pop(0))
    if len(q) == 0:
        print("EMPTY")
    else:
        print(q[-1], q[0])


"""
1
7
I 3
I 2
I 1
I 4
D 1
D 1
D -1
정답 : 2 2

1
12
I 9
I 7
I 9
I 6
I 7
I 7
I 9
D -1
D 1
I 8
D 1
D 1
정답 : 8 7
"""

