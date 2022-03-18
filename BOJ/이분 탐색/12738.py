# 가장 긴 증가하는 부분 수열 3
# 가장 긴 증가하는 부분 수열 2 + 음수 가능

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stack = []
def binarySearch(stack, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if stack[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in lst:
    if len(stack) == 0:
        stack.append(i)
        continue
    if stack[-1] < i:
        stack.append(i)
    # elif stack[0] > i:
    #     stack.insert(0, i)
    else:
        idx = binarySearch(stack, i, 0, len(stack)-1)
        # stack.insert(idx, i)   # 동일한 값이 중복으로 list에 들어감
        stack[idx] = i   

print(len(stack))