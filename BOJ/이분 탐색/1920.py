# 수 찾기

import sys
input = sys.stdin.readline

n = int(input())
lstA = list(map(int, input().split()))
lstA.sort()
m = int(input())
lstM = list(map(int, input().split()))

def binarySearch(lstA, lstM):
    for i in lstM:
        check = False
        start = 0
        end = len(lstA) - 1
        while start <= end:
            mid = (start + end) // 2
            if i == lstA[mid]:
                check = True
            if i >= lstA[mid]:
                start = mid + 1
            else:
                end = mid - 1
        if check: print(1)
        else: print(0)

binarySearch(lstA, lstM)