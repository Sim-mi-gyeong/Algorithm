# 두 수의 합
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
target = int(input())
lst.sort()
cnt = 0
start, end = 0, n-1

while start < end:
    tmpSum = lst[start] + lst[end]
    if tmpSum == target:
        cnt += 1
        start += 1
    elif tmpSum > target:
        end -= 1
    else:
        start += 1
print(cnt)