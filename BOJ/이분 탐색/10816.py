# 숫자 카드 2

from bisect import bisect_left, bisect_right

n = int(input())
lstN = list(map(int, input().split()))
lstN = sorted(lstN)
m = int(input())
lstM = list(map(int, input().split()))

def countExist(lst, leftValue, rightValue):
    right = bisect_right(lst, rightValue)
    left = bisect_left(lst, leftValue)
    return right - left

for i in lstM:
    cnt = countExist(lstN, i, i)
    print(cnt, end = ' ')