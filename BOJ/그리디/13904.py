# 과제

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
lst.sort(key=lambda x: x[1], reverse=True)
ans = 0
visited = [0] * 1001
for d, w in lst:
    i = d
    if visited[i]:
        while visited[i]:
            i -= 1
    if i > 0 and not visited[i]:
        visited[i] = 1
        ans += w


print(ans)
