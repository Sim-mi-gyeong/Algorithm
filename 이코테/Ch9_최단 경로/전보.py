# 통로는 방향성이 있는 간선
# 모든 도시가 메시지를 받아야 함

# 3 2 1
# 1 2 4
# 1 3 2

# 도시의 개수, 통로의 개수, 메시지 보내고자 하는 도시
import sys
input = sys.stdin.readline
n, m, c = map(int, input().split())
start = c

edge = [[] for _ in range(n+1)]
INF = 1e9
distance = [INF] * (n+1)
visited = [False] * (n+1)

for i in range(m):
    x, y, z = map(int, input().split())
    # X 도시에서 -> 다른 도시 Y 로 이어지는 통로가 존재하며, 이때 전달되는 시간이 Z
    edge[x].append((y, z))

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if min_value > distance[i] and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in edge[start]:
        distance[j[0]] = j[1]

    for i in range(n-1):
        now = get_smallest_node()    # 현재 노드에서 거리가 가장 짧은 노드
        visited[now] = True
        for j in edge[now]:
            cost = distance[now] + j[1]   
            if cost < distance[j[0]]:    # 현재 노드에서 + 다음 노드까지 거리가, 거리 테이블의 값보다 작은 경우
                distance[j[0]] = cost
dijkstra(start)

cnt = 0
time = 0
for i in range(1, len(visited)):
    if visited[i] == True:
        cnt += 1
        time = max(distance[i], time)

print(cnt-1, time)

# INF = int(1e9)   # 무한을 의미하는 값으로 10억 설정

# # 노드의 개수 및 간선의 개수를 입력받기
# n, m, c = map(int, input().split())
# start = c
# graph = [[INF] * (n+1) for _ in range(n+1)]

# for a in range(1, n+1):
#     for b in range(1, n+1):
#         if a == b: graph[a][b] = 0 

# for _ in range(m):
#     x, y, z = map(int, input().split())
#     graph[x][y] = z

# for k in range(1, n+1):
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# cnt = 0
# time = 0
# for i in range(1, n+1):
#     if graph[start][i] != INF and start != i:
#         cnt += 1
#         time = max(time, graph[start][i])
# print(cnt, time)