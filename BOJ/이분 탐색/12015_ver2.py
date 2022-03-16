# 가장 긴 증가하는 부분 수열 2
# target 원소가 들어갈 위치 : bisect_left 함수 사용

from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stack = [0]

for i in lst:
    if stack[-1] < i:
        stack.append(i)
    else:
        stack[bisect_left(stack, i)] = i
print(len(stack) - 1)