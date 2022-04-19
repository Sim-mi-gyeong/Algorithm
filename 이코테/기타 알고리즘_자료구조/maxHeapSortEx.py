# 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예시

import sys
import heapq  # python 은 기본적으로, Min heap 형태로 동작(오름차순 정렬) -> Max Heap으로 동작하기 위해서는 데이터를 넣을 때와 꺼낼 때 ' - ' 사용

input = sys.stdin.readline


def heapSort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -1 * value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-1 * heapq.heappop(h))

    return result


n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapSort(arr)

for i in range(n):
    print(res[i])

