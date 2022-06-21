# 부분수열의 합(2^n)

import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
result = dict()


def dfs(depth, number):
    if depth == n:
        if number not in result:
            result[number] = 0
        return

    dfs(depth + 1, number + lst[depth])  # 사용하는 경우
    dfs(depth + 1, number)  # 사용하지 않는 경우


dfs(0, 0)

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
