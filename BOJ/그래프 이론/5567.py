# 결혼식

from collections import deque

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)

cnt = 0


def bfs(start):
    global cnt
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        v = q.popleft()
        # 자신의 친구에 대해
        for i in graph[v]:
            if visited[i] == 0 and visited[v] <= 2:
                visited[i] = visited[v] + 1
                cnt += 1
                # print("i : ", i, " cnt : ", cnt, "  visitied[i] : ", visited[i])
                q.append(i)

    return cnt


print(bfs(1))
