# 최대 힙
import heapq

# 내림차순 힙 정렬(Heap Sort)
# 데이터의 부호를 바꾸어서 넣고, 바꾸어서 꺼내기
# 내부적으로 최대힙을 구하는 것과 같음
def heapSort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapSort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)