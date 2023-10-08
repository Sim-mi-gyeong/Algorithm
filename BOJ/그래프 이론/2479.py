# 경로 찾기

from collections import deque
import heapq

n, k = map(int, input().split())
dic = dict()
graph = [[] for _ in range(n + 1)]
for i in range(n):
    s = input()
    dic[i + 1] = s
    graph[i + 1].append(s)

start, end = map(int, input().split())

d = [] * (n + 1)
dir = [] * (n + 1)


def bfs():
    q = deque()
