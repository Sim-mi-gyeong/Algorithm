import heapq
import sys
from winreg import ConnectRegistry
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력 받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력 받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(n+1)]
# # 방문한 적이 있는지 체크하는 목적의 리스트 만들기 -> 필요 X
# visited = [False] * (n+1)
# 최단 거리 테이블을모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a 번 노드에서 -> b 번 노드로 가는 비용이 c 임을 의미
    graph[a].append((b,c))

# 매번, 현재 상황에서 가장 최단 거리가 짧은 노드를 구하기 위한 함수가 별도로 사용되지 X

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0 으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:   # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappush(q)   # (거리, 현재 노드)
        # 현재 노드가 이미 처리된 적이 있는 노드라면(꺼낸 노드의 거리 값이, 테이블에 기록된 값보다 크다면), 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappushq, (cost, i[0])

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우, 거리 출력
    else:
        print(distance[i])