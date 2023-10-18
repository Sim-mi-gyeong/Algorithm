import sys

input = sys.stdin.readline

l, n, q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(l)]
