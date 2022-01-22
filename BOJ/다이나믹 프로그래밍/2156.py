# 포도주 시식

# 연속으로 선택 불가능한 경우 - 해당 위치 선택 여부 -> 그 이전을 선택했거나, 하지 않았거나

# [i번째 위치 선택 O or X]
# 1. i번째 선택 O
# d[i] = (d[i-2] + arr[i]) or (d[i-3] + arr[i-1] + arr[i])
#   1) i-1 번째 선택 O
#   2) i-1 번째 선택 X
# 2. i번째 선택 X -> d[i-1]

n = int(input())
lst = [int(input()) for _ in range(n)]
d = [0] * n
if n == 1: 
    d[0] = lst[0]
elif n == 2: 
    d[0] = lst[0]
    d[1] = lst[0] + lst[1]
else:
    d[0] = lst[0]
    d[1] = d[0] + lst[1]
    for i in range(2, n):
        d[i] = max(d[i-2] + lst[i], d[i-3] + lst[i-1] + lst[i], d[i-1])

print(d[n-1])