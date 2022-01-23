# 연속합

n = int(input())
lst = list(map(int, input().split()))
d = [0] * n
d[0] = lst[0]

for i in range(1, n):
    if d[i-1] + lst[i] >= lst[i]:
        d[i] = d[i-1] + lst[i]
    else:
        d[i] = lst[i]
    # if d[i-1] < d[i-2]:
    #     d[i] = lst[i]
    # if d[i-2] + d[i-1] > lst[i]:
    #     d[i] = d[i-1] + lst[i]
print(max(d))