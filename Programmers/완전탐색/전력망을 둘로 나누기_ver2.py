# BFS

from collections import deque


def bfs(start, deleted, visited, graph):
    q = deque()
    visited[start] = 1
    q.append(start)
    cnt = 1

    while q:
        curr = q.popleft()
        for i in graph[curr]:
            if not visited[i] and i != deleted:
                cnt += 1
                visited[i] = 1
                q.append(i)

    return cnt


def solution(n, wires):
    answer = 1e9

    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    for a, b in wires:
        visited = [0] * (n + 1)

        # a, b 중 하나를 잘랐을 때 -> 미리 방문 처리를 해서 BFS 탐색 범위에 포함되지 않도록
        visited[b] = 1
        cnt = bfs(a, b, visited, graph)  # 한쪽 연결 그래프에 포함된 노드(송전탑) 개수
        another = n - cnt

        diff = abs(cnt - another)
        if diff < answer:
            answer = diff

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
# print(solution(4, [[1, 2], [2, 3], [3, 4]]))
# print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))
