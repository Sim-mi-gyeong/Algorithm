# 가장 긴 증가하는 부분 수열 3
# 가장 긴 증가하는 부분 수열 2 + 음수 가능

import sys
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
stack = []

for i in lst:
    if len(stack) == 0:
        stack.append(i)
        continue
    if stack[-1] < i:
        stack.append(i)
    # elif stack[0] > i:
    #     stack.insert(0, i)
    #     # stack[0] = i
    else:
        stack[bisect_left(stack, i)] = i   

print(len(stack))