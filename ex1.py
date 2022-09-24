n, m = map(int, input().split())
lst = list(map(int, input().split()))

###
cnt = 0
tmpSum = 0
end = 0
for start in range(n):
    # tmpSum 이 조건을 만족시키지 않으면, start 를 늘리고 -> 이전 while 에서 값이 저장된 end 부터 시작
    while tmpSum < m and end <= n - 1:
        tmpSum += lst[end]
        end += 1
    if tmpSum == m:
        cnt += 1

    tmpSum -= lst[start]


print(cnt)

###
cnt = 0
for start in range(n):
    tmpSum = lst[start]
    end = start + 1
    # start 부터 end 까지 tmpSum == m 을 한 번 만족하고 나서 -> end 를 늘려 값을 더하는 것은,
    # 어차피 조건을 만족시키지 못함 -> 시간초과
    while end < n:
        if tmpSum == m:
            cnt += 1
        tmpSum += lst[end]
        end += 1

print(cnt)
