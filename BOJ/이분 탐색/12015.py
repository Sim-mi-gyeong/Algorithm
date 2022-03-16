# 가장 긴 증가하는 부분 수열 2
# 가장 큰 증가 부분 수열에 비해 수열 A 의 크기 N 이 1000 배 크다(큰 범위)

# By BinarySearch -> 수열이 들어갈 자리 찾기
# for 문에서, 현재 원소(target) > stack의 마지막 원소 -> 수열 연장 가능 -> stack 마지막에 추가
# 그렇지 않은 경우, 들어갈 자리 찾기

import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
stack = [0]

# lst 의 원소가 들어갈 위치를 찾기 위한 func
def binarySearch(lst, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if stack[mid] < target:
            start = mid + 1
        else: 
            end = mid - 1
    # stack 에서 mid 의 위치 다음에, target 원소가 위치하게 되므로, 
    # mid + 1 처리가 된 return start
    return start

for i in lst:
    if stack[-1] < i:
        stack.append(i)
    else:
        # 원소가 수열에 들어갈 수 있는 위치 탐색 in stack
        idx = binarySearch(lst, i, 0, len(stack)-1)
        stack[idx] = i

print(len(stack) - 1)

# import sys
# input = sys.stdin.readline

# n = int(input())
# lst = list(map(int, input().split()))
# start, end = 0, len(lst)
# dp = [x for x in lst]
# dp2 = [1] * n
# def binarySearch(lst, start, end):
#     while start <= end:
#         mid = (start + end) // 2
#         tmpSum = 0
#         for i in range(1, n):
#             for j in range(0, i):
#                 if lst[j] < lst[i]:
#                     dp2[i] = max(dp2[i], dp2[j] + 1)
#         tmpSum = max(tmpSum, max(dp2))
#         if tmpSum <= mid:
#             result = max(dp2)
#             start = mid + 1
#         else:
#             end = mid - 1
#     return result

# print(binarySearch(lst, start, end))

# 위의 풀이에서 아래 TC 확인
'''
[입력 예시]
8
10 20 30 5 10 20 30 40
[출력 예시]
5
'''