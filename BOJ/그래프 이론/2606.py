# 바이러스

n = int(input())
m = int(input())
graph = [[] * (n + 1) for _ in range(n + 1)]
cnt = 0
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [False] * (n + 1)

def dfs(graph, v, visited):
  global cnt
  visited[v] = True
  for i in graph[v]:
    if not visited[i]:
      cnt += 1
      dfs(graph, i, visited)
dfs(graph, 1, visited)
print(cnt)