# 최단경로
# 우선순위 큐 이용
# 정점의 개수, 간선의 개수
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
v, e = map(int, input().split())
start = int(input())
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)

for _ in range(e):
    # u에서 -> v로 가는, 가중치 w
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)   # 현재 노드
        # 현재 노드가 이미 처리된 적이 있는 노드라면(꺼낸 노드의 거리 값이, 테이블에 기록된 값보다 크다면), 무시
        if dist > distance[now]:
            continue
        for i in graph[now]:   # 현재 노드와 연결된 노드 확인
            # 현재 노드까지의 거리 + 현재 노드 -> 현재 노드와 연결된 노드까지의 거리
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(start)
for d in distance[1:]:
    if d == INF: print('INF')
    else: print(d)