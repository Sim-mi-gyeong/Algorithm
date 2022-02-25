# 숨바꼭질

from collections import deque

n, k = map(int, input().split())
visited = [-1] * 100001

def bfs(start, visited):
    queue = deque([])
    queue.append(start)
    if visited[start] == -1:
        visited[start] = visited[start] + 1
    while queue:
        v = queue.popleft()
        lst = [v-1, v+1, v*2]
        for i in lst:
            if 0 <= i <= 100000 and visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)  
            if i == k and visited[k] != -1:
                return visited[k]

print(bfs(n, visited))
