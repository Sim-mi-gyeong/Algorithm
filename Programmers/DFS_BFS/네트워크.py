from collections import deque

n = int(input())
com = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
visited = [0] * (n)
cnt = 0
def bfs(com, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in range(len(com[v])):
            if visited[com[v][i]] == 0: 
                visited[com[v][i]]= 1
                queue.append(visited[com[v][i]])
                # cnt += 1
                # visited[v[i]] = 0
                # queue.append(visited[v[i]])
    print(visited)
    for i in visited: 
        if i == 0: cnt += 1
    # cnt += 1

bfs(com, 0, visited)
print(cnt)
# graph = [[] * (n+1) for _ in range(n+1)]
# for i in com:
#     print(i)
#     for j in i:
#         print(j)
#         # if j == 1:
#         #     graph[i].append(i[j])
# print(graph)
        # a, b = map(int, input().split())
        # graph[a].append(b)
        # graph[b].append(a)