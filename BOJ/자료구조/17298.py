# 오큰수

n = int(input())
lst = list(map(int, input().split()))
stack = []
ans = [-1] * n
stack.append(0)

for i in range(1, n):
    while len(stack) != 0 and lst[i] > lst[stack[-1]]:   # while stack and ~
        ans[stack.pop()] = lst[i]
    stack.append(i)
print(*ans)