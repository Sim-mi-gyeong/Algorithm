# 부분합

n, s = map(int, input().split())
lst = list(map(int, input().split()))
start, end = 0, 0
sumValue = 0
ans = 1000001

if sumValue >= s:
    print(1)
    exit(0)

while True:
    if sumValue >= s:
        ans = min(ans, end - start)
        sumValue -= lst[start]
        start += 1
    elif end == n or start == n:
        break
    else:
        sumValue += lst[end]
        end += 1

if ans != 1000001:
    print(ans)
else: print(0)