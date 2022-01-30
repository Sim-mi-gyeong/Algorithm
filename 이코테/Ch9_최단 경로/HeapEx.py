# 최소 힙(기본적으로 최소 힙으로)
import heapq

# 오른차순 힙 정렬
def heapSort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

result = heapSort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# 힙은 데이터를 넣을 때, 뺄 때 시간 복잡도가 O(logN) 이므로
# 데이터를 넣었다 빼면 O(NlongN)의 시간 복잡도를 가짐.(최악의 경우에도 보장)