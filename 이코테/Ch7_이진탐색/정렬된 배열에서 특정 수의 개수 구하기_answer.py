# 문제 해결 아이디어
# 시간 복잡도 O(logN)으로 동작하는 알고리즘 요구
# 일반적인 선형 탐색(Linear Search)로는 시간 초과 판정
# 데이터가 정렬 -> 이진 탐색 수행 가능
# 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아 -> 위치 차이 계산해 문제 해결

# 처음 전체 범위에 대해 이진 탐색을 2번 수행
# 이진 탐색 1: 첫 위치 / 이진 탐색 2: 마지막 위치를 찾도록 수행

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_range(array, x, x)
if count == 0: print(-1)
else: print(count)