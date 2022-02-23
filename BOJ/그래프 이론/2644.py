# 촌수 계산

import sys
sys.setrecursionlimit(10**6)

n = int(input())   # 전체 사람 수
a, b = map(int, input().split())   # 구해야 하는 두 사람의 촌수
m = int(input())   # 부모 자식들 간의 관계의 개수
lst = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())   # x 는 y 의 부모
    lst[x].append(y)
    lst[y].append(x)
visited = [0] * (n+1)

def dfs(start, lst, visited):
    global cnt, b
    for i in lst[start]:
        if visited[i] == 0:
            visited[i] = visited[start] + 1
            dfs(i, lst, visited)

dfs(a, lst, visited)
if visited[b] == 0: print(-1)
else: print(visited[b])