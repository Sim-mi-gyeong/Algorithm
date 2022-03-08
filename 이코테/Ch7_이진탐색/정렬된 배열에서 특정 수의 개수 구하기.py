# N개의 원소를 포함하고 있는 수열이 오름차순 정렬
# 이 수열에서 x가 등장하는 횟수 계산
# 시간 복잡도 O(logN)으로 알고리즘 설계하기
from bisect import bisect_left, bisect_right
n, m = map(int, input().split())
lst = list(map(int, input().split()))

def count(arr, left, right):
    left_idx = bisect_left(arr, left)
    right_idx = bisect_right(arr, right)
    return right_idx - left_idx
print(count(lst, m, m))

'''
[입력 예시]
7 2
1 1 2 2 2 2 3
[출력 예시]
4
'''