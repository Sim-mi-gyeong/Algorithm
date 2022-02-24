# 효율적인 해킹

import sys
input = sys.stdin.readline

n, m = map(int, input().split())    # n : 컴퓨터 수, m : 관계 수
rel = [[] for _ in range(n+1)]
rel2 = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for i in range(m):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)
    rel2[a].append(b)
print('rel : ', rel)
print('rel2 : ', rel2)
resutl = []

from collections import deque
queue = deque([])
start = n
# def bfs(start, rel, visited):
#     queue.append(start)
#     visited[start] += 1
#     while queue:
#         v = queue.popleft()
#         for i in rel[v]:
#             if visited[i] == 0:   # 방문하지 않았으면, 
#                 visited[i] = visited[v] + 1
#                 queue.append(i)

def bfs(start, rel, visited):
    queue.append(start)
    visited[start] = 1
    cnt = 1
    while queue:
        v = queue.popleft()
        for i in rel[v]:
            if visited[i] == 0:   # 방문하지 않았으면, 
                visited[i] = 1
                queue.append(i)
                cnt += 1
    return cnt

print('bfs : ' , bfs(start, rel, visited))

print(visited)
