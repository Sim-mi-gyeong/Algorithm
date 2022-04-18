# ACM Craft
from collections import deque


def topologySort():
    queue = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            queue.append((i, time[i]))
            result[i] = time[i]

    newTime = 0  # 전체 합산에 대한 시간 변수
    while queue:
        now, beforeTime = queue.popleft()
        if now == w:
            return result[now]

        currentTime = 0  # 같은 열에서 선택지가 다를 경우 최댓값을 저장하기 위한 시간 변수
        # newTime = 0
        for j in graph[now]:
            indegree[j] -= 1
            if indegree[j] == 0:
                currentTime = max(currentTime, time[j])
                newTime = max(newTime, beforeTime + currentTime)
                queue.append((j, newTime))
                result[j] = newTime
            else:
                currentTime = max(currentTime, time[j])
                newTime = max(newTime, beforeTime + currentTime)


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
4 3
1 1 1 1
1 2
3 2
1 4
4

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
