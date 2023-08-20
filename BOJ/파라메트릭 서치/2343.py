N, M = map(int, input().split())
lst = list(map(int, input().split()))

ans = 0
left, right = max(lst), sum(lst)
while left <= right:
    mid = (left+right)//2

    cnt, sum = 0, 0
    for i in range(N):
        if sum + lst[i] > mid:
            cnt += 1
            sum = 0
        sum += lst[i]
    if sum:
        cnt += 1

    if cnt > M:
        left = mid + 1
    else:
        right = mid - 1
        ans = mid

print(ans)