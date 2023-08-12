# 끝나지 않는 파티

import sys

input = sys.stdin.readline
n, m = map(int, input().split())

graph = [[0] * n for _ in range(n)]
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        graph[i][j] = tmp[j]

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


def check(src, dst, time):
    if graph[src - 1][dst - 1] <= time:
        return True
    return False


for _ in range(m):
    a, b, c = map(int, input().split())

    if check(a, b, c):
        print("Enjoy other party")
    else:
        print("Stay here")
