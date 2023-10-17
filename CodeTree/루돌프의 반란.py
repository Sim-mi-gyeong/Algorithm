import sys

input = sys.stdin.readline

n, m, p, c, d = map(int, input().split())

graph = [[0] * n for _ in range(n)]
sx, sy = map(int, input().split())
sx -= 1
sy -= 1

for _ in range(p):
    num, x, y = map(int, input().split())
    graph[x - 1][y - 1] = num
