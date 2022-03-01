# 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**9)

n = int(input())
lst = [[] * (n + 1) for _ in range(n + 1)]
for i in range(n-1):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

parent = [0] * (n+1)

def dfs(start, lst, parent):
    for i in lst[start]:
        if parent[i] == 0:
            parent[i] = start
            dfs(i, lst, parent)
dfs(1, lst, parent)
for i in range(2, len(parent)):
    print(parent[i])