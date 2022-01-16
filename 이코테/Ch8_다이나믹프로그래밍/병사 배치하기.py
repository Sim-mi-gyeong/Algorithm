# 전투력이 높은 병사가 앞쪽에 오도록 내림차순 배치
# 남아 있는 병사의 수가 최대가 되도록 하기 위해 열외시켜야 하는 병사의 수
# 각 병사의 전투력은 10,000,000 보다 작거나 같은 자연수 => 의미 : 

# 시간 제한 : 1초 & n <= 2000 -> O(N^2) 이하인 시간 복잡도를 가지도록
n = int(input())
per = list(map(int, input().split()))

d = [0] * n
d[0] = per[0]  
for i in range(1, n):
    if per[i-1] > per[i]:
        if per[i] < per[i+1]:
            d[i] = 0
        else:
            d[i] = per[i]
    else:
        d[i] = per[i]

cnt = 0
for i in d[1:]:
    if i == 0: cnt += 1