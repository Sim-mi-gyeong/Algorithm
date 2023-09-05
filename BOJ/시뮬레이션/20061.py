# 모노미노도미노 2

import sys

input = sys.stdin.readline
n = int(input().rstrip())


def move_green(t, x, y):
    pass


def move_blue(t, x, y):
    pass


total = 0


def solve(t, x, y):
    global total
    pass


for _ in range(n):
    t, x, y = map(int, input().rstrip().split())
    solve(t, x, y)

graph = [[0] * 10 for _ in range(10)]

for i in range(4):
    for j in range(4):
        graph[i][j] = 1

for i in range(4, 10):
    for j in range(4):
        graph[i][j] = 2

for i in range(4):
    for j in range(4, 10):
        graph[i][j] = 3
