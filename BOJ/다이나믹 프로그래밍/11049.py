# 행렬 곱셈 순서

n = int(input())  # 행렬의 개수

lst = [list(map(int, input().split())) for _ in range(n)]

# 곱셈의 최소 곱셈 횟수 기록
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    pass
