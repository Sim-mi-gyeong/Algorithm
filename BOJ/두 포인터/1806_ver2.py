# 부분합

n, s = map(int, input().split())
lst = list(map(int, input().split()))
sumValue = lst[0]   # 초기합 설정
end = 0
ans = 1000001

# 반복문도 시작하기 전에, 조건 만족하는 경우 예외 처리
if sumValue >= s:
    print(1)
    exit(0)
for start in range(n):
    while sumValue < s and end < n:
        end += 1
        if end == n:
            break
        sumValue += lst[end]     
        
    if sumValue >= s:
        ans = min(ans, end - start +  1)
        sumValue -= lst[start]

if ans != 1000001: print(ans)
else: print(0)