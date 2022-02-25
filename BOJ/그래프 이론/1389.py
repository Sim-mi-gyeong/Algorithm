# 케빈 베이컨의 6단계 법칙
# 최대 6단계 이내에서 서로 아는 사람으로 연결 가능
from collections import deque

n, m = map(int, input().split())
rel = [[] * m for _ in range((n+1))]

for i in range(m):
    a, b = map(int, input().split()) 
    rel[a].append(b)
    rel[b].append(a)

def bfs(start, rel, visited):
    queue = deque([])
    queue.append(start)
    if visited[start] == -1:
        visited[start] = 0
        
    while queue:
        v = queue.popleft()  
        for i in rel[v]: 
            if visited[i] == -1:
                visited[i] = visited[v] + 1
                queue.append(i)
                
    return visited

result = []
minTotal = 1e9
for i in range(1, n+1):
    visited = [-1] * (n+1)
    ans = bfs(i, rel, visited)
    total = sum(ans[1:])
    if minTotal > total: 
        minTotal = total
    result.append([i, total])

for i, total in result:
    if total == minTotal:
        print(i)
        exit(0)