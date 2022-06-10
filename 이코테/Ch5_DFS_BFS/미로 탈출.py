# n, m = map(int, input().split())
# graph = []
# for i in range(n):
#     graph.append(list(map(int, input())))

# cnt = 1
# def dfs(x, y):
#     if x < 0 or x >= n or y < 0 or y >= m:
#         return False
#     if graph[x][y] == 1:
#         print((x, y))
#         graph[x][y] = 0
   
#         dfs(x + 1, y)
#         dfs(x, y + 1)
#         # dfs(x - 1, y)
#         # dfs(x, y - 1)
#         return True   # 연결된 노드가 1이 맞을 때마다 True를 반환하도록 해야함 

# for i in range(n):
#     for j in range(m):
#         print(dfs(i, j))
#         if dfs(i, j):
#             cnt += 1

# print(cnt)

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]   # x 좌표를 행처럼
dy = [0, 0, -1, 1]   # y 좌표를 열처럼

def bfs(x, y):
    # queue = deque([graph[x][y]])
    queue = deque()
    queue.append(graph[x][y])

    while queue:
        v = queue.popleft()
        for k in range(4):
            x += dx[k]
            y += dy[k]
            if x < 0 or y < 0 or x >= n or y >= m:
                continue
            if graph[x][y] == 0:
                continue
            if graph[x][y] == 1:
                graph[x][y] = v + 1
                queue.append(graph[x][y])
                print(queue)

    return graph[x][y]

    # if graph[x][y] != 0:
    #     # queue.append(graph[x][y])
    #     v = queue.popleft()
        
print(bfs(0, 0))