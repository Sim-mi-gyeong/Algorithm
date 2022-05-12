# 주유소

n  = int(input())   # 도시 개수
d = list(map(int, input().split()))    # 각 도시간 거리
w = list(map(int, input().split()))   # 각 도시에서 리터 당 주유 금액
target = sum(d)   # 6리터
# d 각각의 요소 * w 각각의 요소 (인덱스 0부터)
# 일단, 처음에 d[0]만큼은 무조건 넣어야 하고
# 그 다음 남은 거리인 target - d[0] 에 대해
# 두 번째에선 d[1] <= 주유 양 <= target - d[0]은 넣어야 함
 
ans = 0   # 최소 비용
min_w = min(w[:-1])
 
for i in range(len(d)):
    if w[i] <= min_w:
        ans += target * w[i]
        break
    else:
        ans += d[i] * w[i]
        target -= d[i]
print(ans)