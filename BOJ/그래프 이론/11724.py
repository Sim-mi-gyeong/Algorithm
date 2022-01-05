# 11724번 연결 요소의 개수

from collections import deque
n, m = map(int, input().split())
graph = [[] * (n+1) for _ in range(n+1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)
visited = [0] * (n+1)
visited[0] = 1
cnt = 0

def bfs(graph, start, visited):
  global cnt
  queue = deque([start])
  visited[start] = 1

  while queue:
    v = queue.popleft()
    for i in graph[v]:
      if visited[i] == 0:
        queue.append(i)          
        visited[i] = 1

  cnt += 1
  try:
    idx = visited.index(0)
    bfs(graph, idx, visited)
  except:
    pass
 
bfs(graph, 1, visited)
print(cnt)