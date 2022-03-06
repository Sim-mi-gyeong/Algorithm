# 부분합
# 80% 정도에서 틀림 - 웬만한 반례 다 통과

n, s = map(int, input().split())
lst = list(map(int, input().split()))
sumValue = 0 
cnt = 0
end = 0
ans = 1000001

for start in range(n):
    while sumValue <= s and end < n:
        cnt += 1
        sumValue += lst[end]
        end += 1

    if sumValue >= s:
        ans = min(cnt, ans)

    sumValue -= lst[start]
    cnt -= 1

if ans != 1000001: print(ans)
else: print(0)

# 10 0
# 1 1 1 1 1 1 1 1 1 1
# 예상출력 : 1

# 10 100
# 5 1 3 5 10 7 4 9 2 8

# 10 10
# 3 3 3 3 3 3 3 3 3 3
# 4

# 10 10
# 1 1 1 1 1 1 1 1 1 10
# 1