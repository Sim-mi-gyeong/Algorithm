# 중량제한 - 다익스트라 & 최대 힙

import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
distance = [0] * (n+1)   # 최대인 중량을 구하므로 0으로 초기화
for _ in range(m):
    a, b, cost = map(int, input().split())
    lst[a].append((cost, b))
    lst[b].append((cost, a))

start, end = map(int, input().split())

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)   # 0, 1   # 최대 힙 -> dist 값이 힙 안에 - 처리 된 상태
        dist = -1 * dist

        # if now == end:   # 현재 목표 지점 노드를 꺼낸 경우 종료
        #     print(dist)
        #     break

        if distance[now] > dist:   # 이미 최대 중량
            continue
        
        for i in lst[now]:   # (5, 2), (3, 3), (3, 4)
            if dist == 0:   # 꺼낸(현재) 노드까지의 중량이 0인 경우(start에 해당하는 경우)
                distance[i[1]] = i[0]   # 다음 노드까지 가는 중량이 바로 distance 테이블에 저장
                heapq.heappush(q, (-distance[i[1]], i[1]))
            # 기존에 테이블에 저장된 값이, dist(이전 도시에서 최대 중량)와 현재 다리의 최대 중량(i[0]) 보다 작다면
            # 테이블 저장 값 / dist(이전 도시 최대 중량) / i[0](현재 도시 최대 중량) 세 가지 고려
            elif distance[i[1]] < i[0] and distance[i[1]] < dist:   # 다음으로 나가아가고자 하는 노드까지 이미 저장된 중량 테이블 값이 < 다음 노드까지 가능한(큐에서 꺼낸) 값보다 작은 경우
                distance[i[1]] = min(i[0], dist)   # 이전 노드까지의 최대 중량과, 현재 다리의 최대 중량 중 작은 값이 저장
                heapq.heappush(q, (-distance[i[1]], i[1]))

dijkstra(start, end)
print(distance[end])

"""
4 6
1 2 2
2 4 9
4 3 3
2 3 10
1 3 8
3 4 7
1 4
"""