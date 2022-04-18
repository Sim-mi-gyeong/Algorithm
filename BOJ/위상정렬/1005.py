# ACM Craft
from collections import deque
import sys

input = sys.stdin.readline


def topologySort():
    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append((i, time[i]))
            result[i] = time[i]

    while queue:
        now, beforeTime = queue.popleft()
        if now == w:
            return result[now]

        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                # 걸리는 시간의 최댓값이 result 테이블에도 저장한 상태! -> 새로 변수를(currentTime 등) 생성해 max 비교하지 않아도 됨
                newTime = max(result[j], result[now] + time[j])
                queue.append((j, newTime))
                result[j] = newTime
            else:  # indegree -= 1 이후에도 0이 되지 않는 경우
                newTime = max(result[j], result[now] + time[j])
                result[j] = newTime


t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    graph = [[] * (n + 1) for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    for i in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b] += 1
    w = int(input())
    result = [0] * (n + 1)
    print(topologySort())


"""
1
3 2
1 1 1
2 3
1 2
3
정답 : 3

1
7 6
8 1 1 1 1 1 1
1 5
2 5
3 6
4 6
5 7
6 7
7
정답 : 10
"""
