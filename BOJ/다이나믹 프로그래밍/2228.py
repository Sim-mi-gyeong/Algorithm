# 구간 나누기

# m 개의 구간 선택
# 구간에 속한 수들의 총 합 최대

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
INF = 1e9
arr1 = [[0] + [-INF * m for _ in range(n + 1)]]
arr2 = [[0] + [-INF * m for _ in range(n + 1)]]

for i in range(1, n + 1):
    num = int(input())
    for j in range(1, min(m, (i + 1) // 2) + 1):
        arr2[i][j] = max(arr1[i - 1][j], arr2[i - 1][j])
        arr1[i][j] = max(arr1[i - 1][j], arr2[i - 1][j - 1]) + num

print(max(arr1[n][m], arr2[n][m]))
