def solution(n, computers):
    global parent
    answer = 0

    visited = [0] * (n + 1)

    def dfs(start, visited):
        visited[start] = 1

        for idx, val in enumerate(computers[start]):
            # start 노드와 연결(val)되어 있고, 해당 노드(idx)가 아직 방문하지 않은 노드인 경우
            if val == 1 and not visited[idx]:
                dfs(idx, visited)

    for i in range(n):
        if not visited[i]:
            dfs(i, visited)
            answer += 1

    return answer
