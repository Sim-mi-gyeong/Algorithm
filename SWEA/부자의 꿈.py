import sys
si = sys.stdin.readline
n, m, Q = map(int, si().split())
a = [list(map(int, si().split())) for _ in range(n)]
row_max = [[0, 0] for _ in range(n)]
col_max = [[0, 0] for _ in range(m)]
for i in range(n):
    for j in range(m):
        if row_max[i][0] < a[i][j]:
            row_max[i] = [a[i][j], j]
        if col_max[j][0] < a[i][j]:
            col_max[j] = [a[i][j], i]
def is_safe(i, j):
    return row_max[i][1] == j and col_max[j][1] == i
cnt = 0
for i in range(n):
    for j in range(m):
        if is_safe(i, j):
            cnt += 1
ans = 0
for _ in range(Q):
    r, c, v = map(int, si().split())
    r -= 1
    c -= 1
    if is_safe(r, c):
        a[r][c] = v
        ans += cnt
        continue
    if row_max[r][0] < v:
        if is_safe(r, row_max[r][1]):
            cnt -= 1
    if col_max[c][0] < v:
        if is_safe(col_max[c][1], c):
            cnt -= 1
    if row_max[r][0] < v:
        row_max[r][0] = v
        row_max[r][1] = c
    if col_max[c][0] < v:
        col_max[c][0] = v
        col_max[c][1] = r
    if is_safe(r, c):
        cnt += 1
    a[r][c] = v
    ans += cnt
print(ans)