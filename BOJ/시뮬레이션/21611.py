# 마법사 상어와 블리자드

import sys

input = sys.stdin.readline

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

n, m = map(int, input().rstrip().split())
sharkX, sharkY = int(n / 2), int(n / 2)

graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
arr = [0] * (n * n)
num = [[0] * n for _ in range(n)]


def calculate_snail_num():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 0, 0
    dir = 0
    v = n * n - 1

    while v:
        arr[v] = graph[x][y]
        num[x][y] = v
        v -= 1
        while True:
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= n or num[nx][ny] != 0:
                dir = (dir + 1) % 4
                continue
            x, y = nx, ny
            break


def compress():
    lastIdx = 0
    for i in range(1, n * n - 1 + 1):
        if arr[i] == 0:
            continue
        lastIdx += 1
        arr[lastIdx] = arr[i]

    for i in range(lastIdx + 1, n ** 2 - 1 + 1):
        arr[i] = 0


def blizzard(d, s):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    x, y = int(2 / n), int(2 / n)
    for i in range(1, s + 1):
        x += dx[d - 1]
        y += dy[d - 1]

        arr[num[x][y]] = 0

    compress()


def bomb():
    check = False
    return check


def convert():
    pass


cnt = [0] * 4
ans = 0


def pro():
    global m, ans
    calculate_snail_num()
    while m > 0:
        d, s = map(int, input().rstrip().split())
        m -= 1

        blizzard(d, s)

        while bomb:
            pass

        convert()

    for i in range(1, 4):
        ans += i * cnt[i]
    print(ans)


pro()
