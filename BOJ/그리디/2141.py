# 우체국

n = int(input())
lst = [0] * (n + 1)
for _ in range(n):
    a, b = map(int, input().split())
    lst[a] = b

print(lst)
minVal = 1e9
minLoc = n

for i in range(1, n + 1):
    tmpDist = 0
    # 1번 ~ n번 마을까지 돌면서 우체국이 i번 마을에 생길 경우 각 사람까지(마을 간 거리 * 사람 수)의 거리 합
    for j in range(1, n + 1):
        print("i : ", i, " j : ", j, " lst[j] : ", lst[j])
        tmpDist += abs(i - j) * lst[j]
    print("우체국이 ", i, " 위치 일 때 ", " tmpDist : ", tmpDist)
    if tmpDist <= minVal:
        # print("우체국이 ", i, " 위치 일 때 ", " tmpDist : ", tmpDist)
        minVal = tmpDist
        minLoc = i
        # minLoc = min(minLoc, i)

print(minLoc)
