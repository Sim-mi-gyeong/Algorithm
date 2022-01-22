# 플로이드

n = int(input())   # 도시의 수
m = int(input())   # 버스의 수
# lst = [list(map(int, input().split())) for _ in range(m)]    # 시작 도시, 도착 도시, 비용
INF = int(1e9)

ans = [[INF] * n for _ in range(n)]
for i in range(m):
    # a, b, c = i[0], i[1], i[2]
    a, b, c = map(int, input().split())
    if a == b: ans[a-1][b-1] = 0
    if ans[a-1][b-1] > c:
        ans[a-1][b-1] = c   # 작은 금액으로 대체

for k in range(n):
    for i in range(n):
        for j in range(n):
            # 모든 도시의 쌍 (A, B) 의 경로가 존재!!!! -> i > k == 1 and k > j == 1 확인 안 해도 됨.
            if i == j: 
                ans[i][j] = 0
            else:
                ans[i][j] = min(ans[i][j], ans[i][k] + ans[k][j])
for i in ans:
    for j in i: 
        if j == INF:
            print(0, end = ' ')
        else:
            print(j, end= ' ')
    print()