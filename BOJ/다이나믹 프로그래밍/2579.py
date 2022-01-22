# 계단 오르기

# 마지막 도착 계단 반드시 포함 -> i 번째 선택 필수
n = int(input())
lst = [int(input()) for _ in range(n)]
d = [0] * n
if n == 1: d[0] = lst[0]
elif n == 2: d[1] = lst[0] + lst[1]
else:
    for i in range(2, n):
        d[0], d[1] = lst[0], lst[0] + lst[1]
        d[i] = max(d[i-3] + lst[i-1] + lst[i], d[i-2] + lst[i])
print(d[n-1])