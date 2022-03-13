# K 번째 수
# 배열에서 K 번째 수가 x 일 때
# x 미만의 수의 개수 < k
# x 이하의 수의 개수 >= k
# -> k 번째 수에 해당하는 x
# 여기서, 이 x(=mid) 값을 찾기 위해 이분탐색 수행

# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

def count(x):
    und = bel = 0   # 미만의 수, 이하의 수
    for i in range(1, n+1):
        if n * i < x:
            und += n
            bel += n
            continue
        y = x // i
        bel += y
        # x가 i로 완전히 나누어 떨어질 때, 그 수도 포함되므로 -> 미만의 값에서는 -1 처리
        und += y if x % i else y -1
    return und, bel

n = int(input())
k = int(input())
start = 0
end = int(1e10)

while start <= end:
    mid = (start + end) // 2
    und, bel = count(mid)
    if bel < k:
        start = mid + 1
    elif und >= k:   # 너무 큰 수인 상황
        end = mid - 1
    else:   # bel < k and und >= k
        result = mid
        break

print(result)