# 큰 수 구성하기

n, k = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0


def dfs(num, cnt):
    global ans
    if int(num) <= n:
        ans = max(ans, int(num))
        return
    if int(num) > n:
        return
    if num == 0:
        num = ""

    for i in range(int(k)):
        dfs(num + str(lst[i]), cnt + 1)


dfs(0, 0)
print(ans)
