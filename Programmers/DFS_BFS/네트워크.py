from collections import deque

n = int(input())
com = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
visited = [0] * (n)
cnt = 0


def bfs(com, start, visited):
    global cnt
    queue = deque([start])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        for i in range(len(com[v])):
            if visited[com[v][i]] == 0:
                visited[com[v][i]] = 1
                queue.append(visited[com[v][i]])

    print(visited)
    for i in visited:
        if i == 0:
            cnt += 1


bfs(com, 0, visited)
print(cnt)
