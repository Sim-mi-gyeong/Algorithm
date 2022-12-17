from collections import deque

n, m = map(int, input().split())
cnt = 0

# def bfs(graph, start, visited):
#     queue = deque([start])
#     visited[start] = True

#     while queue:
#         v = queue.popleft()
#         # print(v, end = 'v')
#         for i in graph[v]:
#             if graph[v]
#             # if visited[5]
#                 queue.append(graph[])
#     return
def dfs(x, y):
    path = [x-1, x+1, y-1, y+1]   # 상, 하, 좌, 우
    queue = deque()
    if x < 0 or y < 0 or y >= n or y >= m:
        return False
    # for i in range(n):
    #     for j in range(m):
    #         queue.append(graph[i][j])
    while queue:
        x -= 1
        visited[5 * x + y] = True
        y -= 1
        visited[5 * x + y] = True
        x += 1
        visited[5 * x + y] = True
        y += 1
        visited[5 * x + y] = True
        

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

visited = [False] * ( n * m)

# bfs(graph, graph[0][0], visited)
dfs(0, 0)


print(graph)
print(visited)