# 문제 해결 아이디어
# Ex) n = 4 일 때,
# 식량 선택 가능 경우의 수 : 8가지
# ai = (왼쪽부터) i번째 식량 창고까지의 최적의 해(얻을 수 있는 식량의 최댓값)
# DP 테이블의 값은 (최적의 해 계산)
# a0    a1    a2    a3
# 1     3     3     8
# 왼쪽부터 -> 차례대로 식량창고를 턴다고 했을 때, 특정한 i 번째 식량 창고에 대해 털지 안 털지의 여부를 결정하면
# 더 많은 식량을 털 수 있는 경우를 선택하면 됨.

# i 번째 식량창고에 대해 결정을 할 때, i번째는 i-1번째까지의 최적의 해와 i-2번째까지의 최적의 해를 고려해
# 현재의 값에 더한 값과 비교해 더 큰경우를 고름

# 최적 부분의 구조 : 특정 부분까지의 최적의 해는 i-1, i-2번째 까지의 최적의 해를 이용해 계산
# 중복되는 부분 문제 : 

# ai = i번째 식량창고까지의 최적의 해(얻을 수 있는 식량의 최댓값)
# ki = i번째 식량창고에 있는 식량의 양
# 점화식 : ai = max(ai-1, ai-2 + ki)
# 한 칸 이상 떨어진 식량 창고는 항상 털 수 있으므로(이미 앞쪽에서 고려가 된 사항이므로)
# -> (i-3)번째 이하는 고려할 필요 X

n = int(input())
lst = list(map(int, input().split()))
ans = 0

# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

# 다이나믹 프로그래밍 진행(보텀업)
d[0] = lst[0]
d[1] = max(lst[0], lst[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + lst[i])
print(d[n-1])