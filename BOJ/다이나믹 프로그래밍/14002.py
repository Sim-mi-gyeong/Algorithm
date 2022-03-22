# 가장 긴 증가하는 부분 수열 4

n = int(input())
lst = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))

# dp 리스트의 index를 뒤에서부터 -> 가장 큰 max(dp)를 만들게 한 lst의 위치부터 앞으로 추정 가능
stack = []
target = max(dp)
for i in range(n-1, -1, -1):
    if dp[i] == target:
        stack.append(lst[i])
        target -= 1

for i in stack[::-1]: print(i, end = ' ')


'''
6
1 3 5 7 2 3

7
3 1 5 2 3 6 

3
2 4 1
'''