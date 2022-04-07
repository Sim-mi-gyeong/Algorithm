# 게임
# 부동소수점 오차 : https://www.acmicpc.net/board/view/64909

x, y = map(int, input().split())
z = y * 100 // x
# z = math.floor((y / x) * 100)
start, end = 0, 1000000000
# 이진탐색을 수행해도 승률이 달라지지 않는 경우 처리
ans = 0
while start <= end:
    mid = (start + end) // 2
    nextZ = ((y + mid) * 100) // (x + mid)
    if nextZ > z:
        end = mid - 1
        ans = mid
    else:
        start = mid + 1

if ans != 0:
    print(ans)
else:
    print(-1)
