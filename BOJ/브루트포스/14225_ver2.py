# 부분수열의 합 -> 시간초과(n^n)

import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
result = dict()
visited = [0] * (n + 1)


def dfs(depth, number):
    if depth > n:
        return

    if number not in result:
        result[number] = 0

    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, number + lst[i - 1])
            visited[i] = 0


for i in range(1, n + 1):
    visited[i] = 1
    dfs(i, lst[i - 1])


i = 1
while True:
    if i not in result:
        print(i)
        break
    i += 1


"""
10
1 2 3 1 2 3 1 2 3 1

answer : 20
"""
