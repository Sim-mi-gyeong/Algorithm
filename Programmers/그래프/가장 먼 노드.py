from collections import deque


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]
    for idx, vertex in enumerate(edge):
        start, end = vertex[0], vertex[1]
        graph[start].append(end)
        graph[end].append(start)

    INF = int(1e9)
    d = [INF] * (n + 1)

    def bfs(start):
        d[start] = 0
        q = deque([(start, 0)])

        while q:
            curr, dist = q.popleft()
            # if d[curr] > dist:
            #     d[curr] = dist
            for i in graph[curr]:
                if d[i] == INF:  # 아직 방문하지 않은 경우 (이미 방문했다면, 이미 방문했을 때 거리가 더 짧을 것)
                    if d[i] > dist + 1:
                        d[i] = dist + 1
                    q.append((i, dist + 1))

    bfs(1)
    maxVal = max(d[1:])
    for i in range(1, n + 1):
        if d[i] == maxVal:
            answer += 1

    return answer


def solution2(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]
    for idx, vertex in enumerate(edge):
        start, end = vertex[0], vertex[1]
        graph[start].append(end)
        graph[end].append(start)

    d = [-1] * (n + 1)

    def bfs(start):
        d[start] = 0
        q = deque([(start, 0)])

        while q:
            curr, dist = q.popleft()
            for i in graph[curr]:
                if d[i] == -1:
                    q.append((i, dist + 1))
                    d[i] = d[curr] + 1

    bfs(1)
    maxVal = max(d[1:])
    for i in range(1, n + 1):
        if d[i] == maxVal:
            answer += 1

    return answer
