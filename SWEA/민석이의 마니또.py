import sys

si = sys.stdin.readline
n, m = map(int, si().split())
dist = [[-1 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u, v, d = map(int, si().split())
    dist[u - 1][v - 1] = d
for i in range(n):
    for j in range(n):
        for k in range(n):
            if dist[i][k] == -1 or dist[k][j] == -1:
                continue
            t = dist[i][k] + dist[k][j]
            if dist[i][j] == -1:
                dist[i][j] = t
            else:
                dist[i][j] = min(dist[i][j], t)
ans = -1
for i in range(n):
    if dist[i][i] == -1:
        continue
    if ans == -1:
        ans = dist[i][i]
    else:
        ans = min(ans, dist[i][i])
print(ans)
