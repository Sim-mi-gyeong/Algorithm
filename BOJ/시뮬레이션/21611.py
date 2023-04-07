# 마법사 상어와 블리자드
import sys

input = sys.stdin.readline

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
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]
    x, y = int(n / 2), int(n / 2)
    for i in range(1, s + 1):
        x += dx[d]
        y += dy[d]
        arr[num[x][y]] = 0

    compress()


def bomb():
    check = False
    i = 1
    while i <= n * n - 1 + 1:
        if arr[i] == 0:
            break

        j = i
        while j + 1 <= n * n - 1 and arr[i] == arr[j + 1]:
            j += 1

        if j - i + 1 >= 4:
            cnt[arr[i]] += j - i + 1

            for k in range(i, j + 1):
                arr[k] = 0
            check = True

        i = j
        i += 1

    compress()

    return check


def convert():
    b = [0] * (n * n)

    lastIdx = 0

    i = 1
    while i <= n * n - 1 + 1:
        if arr[i] == 0:
            break
        j = i
        while j + 1 <= n * n - 1 and arr[i] == arr[j + 1]:
            j += 1

        A = j - i + 1
        B = arr[i]

        if lastIdx < n * n - 1:
            lastIdx += 1
            b[lastIdx] = A
        if lastIdx < n * n - 1:
            lastIdx += 1
            b[lastIdx] = B

        i = j
        i += 1

    for i in range(1, n * n - 1 + 1):
        arr[i] = b[i]


cnt = [0] * 4
ans = 0


def pro():
    global m, ans
    calculate_snail_num()
    while m > 0:
        d, s = map(int, input().rstrip().split())
        m -= 1

        blizzard(d, s)

        while True:
            flag = bomb()
            if not flag:
                break

        convert()

    for i in range(1, 4):
        ans += i * cnt[i]
    print(ans)


pro()
