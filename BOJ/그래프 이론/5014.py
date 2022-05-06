# 스타트링크

from collections import deque

f, s, g, u, d = map(int, input().split())
graph = [0] * (f + 1)
visited = [0] * (f + 1)
dx = [u, -d]


def bfs():
    queue = deque()
    cnt = 0
    queue.append((s, cnt))
    visited[s] = 1
    check = False
    while queue:
        v, cnt = queue.popleft()
        if v == g:
            check = True
            break
        for i in range(len(dx)):
            nx = v + dx[i]
            if 1 <= nx <= f and not visited[nx] and nx != s:  # 현재 위치가 목표 층인 경우
                # cnt += 1   # 여기에서 cnt += 1 을 하면, 양 방향으로 한 갈래씩 빠지는 것을 모두 count
                visited[nx] = 1
                queue.append((nx, cnt + 1))

    if check:
        return cnt
    else:
        return "use the stairs"


print(bfs())

"""
시작 위치 == 목표 층인 경우
10 1 1 1 1 
"""

