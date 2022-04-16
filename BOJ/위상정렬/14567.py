# 선수과목(Prerequisite)

from collections import deque
import collections
import sys

input = sys.stdin.readline

n, m = map(int, input().split())  # 과목 수, 선수 조건 수
# graph = [[] for _ in range(n + 1)]
graph = collections.defaultdict(list)
indegree = [0] * (n + 1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topologySort():
    result = [0] * (n + 1)
    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append((i, 1))
            result[i] = 1

    while queue:
        now, cnt = queue.popleft()
        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                queue.append((j, cnt + 1))
                result[j] = cnt + 1

    print(*result[1:])


topologySort()
