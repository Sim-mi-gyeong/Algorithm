from collections import deque


def solution(n, computers):
    global parent
    answer = 0

    visited = [0] * n

    def bfs(start, visited):
        visited[start] = 1
        q = deque([start])

        while q:
            curr = q.popleft()
            for i in range(n):
                if computers[curr][i] == 1 and not visited[i]:
                    visited[i] = 1
                    q.append(i)
            # for idx, val in enumerate(computers[curr]):    # faster
            #     if val == 1 and not visited[idx]:
            #         visited[idx] = 1
            #         q.append(idx)

    for i in range(n):
        if not visited[i]:
            bfs(i, visited)
            answer += 1

    return answer
