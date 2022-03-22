# 가장 긴 증가하는 부분 수열 5
# for 문 - 현재 값 > 수열의 마지막 값보다 크다면, stack 에 현재 값 추가
# 가장 긴 부분 수열의 길이(= dp의 index = i 일 때 수열의 길이) 갱신
# No -> stack 부분 수열의 어느 위치에 있는지 이분탐색으로 찾아 -> 해당 값을 갱신

n = int(input())
lst = list(map(int, input().split()))
dp = [0] * n

def binarySearch(stack, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if target > stack[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start

stack = []
for i in range(n):
    if len(stack) == 0:
        stack.append(lst[i])
        dp[i] = len(stack)
    elif stack[-1] < lst[i]:
        stack.append(lst[i])
        dp[i] = len(stack)
    else:
        idx = binarySearch(stack, lst[i], 0, len(stack) - 1)   # 값을 갱신할 위치 -> 해당 값이 마지막일 때 가장 긴 부분 수열 길이 갱신
        stack[idx] = lst[i]
        dp[i] = idx + 1   # 갱신한 값(최장 수열의 길이)

target = max(dp)
ans = []
for i in range(n-1, -1, -1):
    if dp[i] == target:
        ans.append(lst[i])
        target -= 1

print(len(ans))
for i in ans[::-1]: print(i, end = ' ')


'''
4
1 3 4 2
'''