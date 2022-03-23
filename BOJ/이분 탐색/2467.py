# 용액

import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

def binarySearch(lst):
    minValue = 2000000001
    for i in range(len(lst) - 1):
        x1 = i
        start, end = x1 + 1, len(lst) - 1
        while start <= end:
            mid = (start + end) // 2
            sumValue = lst[x1] + lst[mid]
            if abs(sumValue - 0) <= minValue:
                # start = mid + 1
                minX, minY = lst[x1], lst[mid]
                minValue = abs(sumValue - 0)
            if sumValue < 0:
                start = mid + 1
            else:
                end = mid - 1

    return minX, minY   

print(*binarySearch(lst))
        
'''
10
-5 -5 -5 1 1 10 10 10 10 10

4
-100 -2 -1 10

3
999999998 999999999 1000000000

8
-100 -99 99 0 1 2 3 4 5

중앙에서 끝으로 멀어지면 정답이 한쪽에 치우쳐있을때 답을 못찾아옴
8
-1000000 -99 99 100 101 102 103 104 105

7
-99 -2 -1 1 98 100 101
'''