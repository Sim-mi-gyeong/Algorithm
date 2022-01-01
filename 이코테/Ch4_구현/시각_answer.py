# 문제 해결 아이디어
# 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
# python: 1초에 2000 만 번 연산 가능
# 완전 탐색(Brute Forcing) 문제 유형 - 가능한 경우를 모두 검사해보는 탐색 방법

n = int(input())
cnt = 0
for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k) :
                cnt += 1
            # if (i % 10 == 3) or (j // 10 == 3) or (j % 10 == 3) or (k // 10 == 3) or (k % 10 == 3) :
            #     cnt += 1
print(cnt)