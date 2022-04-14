# 연산자 끼워넣기
# 백트래킹

import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))

maxValue = -1e9
minValue = 1e9


def dfs(depth, total, plus, minus, mul, div):
    global maxValue, minValue

    if depth == n:
        maxValue = max(maxValue, total)
        minValue = min(minValue, total)
        print("완료 후 ", "depth : ", depth, " | ", plus, minus, mul, div)
        return  # 빠져나오기

    if plus:
        print("depth : ", depth, " | ", plus, minus, mul, div)
        dfs(depth + 1, total + num[depth], plus - 1, minus, mul, div)

    if minus:
        print("depth : ", depth, " | ", plus, minus, mul, div)
        dfs(depth + 1, total - num[depth], plus, minus - 1, mul, div)

    if mul:
        print("depth: ", depth, " | ", plus, minus, mul, div)
        dfs(depth + 1, total * num[depth], plus, minus, mul - 1, div)

    if div:
        print("depth : ", depth, " | ", plus, minus, mul, div)
        dfs(depth + 1, int(total / num[depth]), plus, minus, mul, div - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maxValue)
print(minValue)
