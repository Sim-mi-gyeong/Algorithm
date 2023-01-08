# 숫자 선물


def dfs(x, y, card, cnt):
    global maxVal
    if card > n:
        return
    if card <= n:
        maxVal = max(maxVal, card)
    if card == 0:
        card = ""
    else:
        card = str(card)
    for i in [x, y]:
        card += str(i)
        dfs(x, y, int(card), cnt + 1)
        card = card[:-1]

    return maxVal


def solve(n, x, y):
    ans = 0
    if n < x and n < y:
        ans = -1
        return ans
    if (x == 0 and y > n) or (x > n and y == 0):
        ans = -1
        return ans
    ans = dfs(x, y, 0, 0)
    return ans


t = int(input())

for tc in range(t):
    n, x, y = map(int, input().split())
    maxVal = 0
    ans = solve(n, x, y)
    print("#{}".format(tc + 1), ans)
