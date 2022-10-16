# 술래잡기


def move(hider, i):
    one_hider = hider[i]
    x, y, dir, alive = one_hider[0], one_hider[1], one_hider[2], one_hider[3]

    if alive == 0:
        return

    nx = x + dx[dir]
    ny = y + dy[dir]

    if not (0 <= nx < n and 0 <= ny < n):
        dir ^= 2

    nx = x + dx[dir]
    ny = y + dy[dir]

    seekX, seekY = seeker[0], seeker[1]
    if (nx, ny) == (seekX, seekY):
        return

    x, y = nx, ny
    hider[i] = (x, y, dir, alive)


def moveHider():
    for i in range(len(hider)):
        one_hider = hider[i]
        x, y = one_hider[0], one_hider[1]
        dist = abs(x - seeker[0]) + abs(y - seeker[1])
        if dist <= 3:
            move(hider, i)


def moveSeek():
    global seeker
    seek_seq_idx = seeker[2]
    next_seq_idx = (seek_seq_idx + 1) % seek_seq_len
    seeker = [seek_seq[next_seq_idx][0], seek_seq[next_seq_idx][1], next_seq_idx]


def catchHider():
    cnt = 0

    seek_seq_idx = seeker[2]

    tmp_dx = seek_seq[seek_seq_idx + 1][0] - seek_seq[seek_seq_idx][0]
    tmp_dy = seek_seq[seek_seq_idx + 1][1] - seek_seq[seek_seq_idx][1]

    for size in range(0, 2 + 1):  # 현재 위치 포함 3칸 이내 범위만 잡을 수 있음
        x = seeker[0] + tmp_dx * size
        y = seeker[1] + tmp_dy * size

        if not (0 <= x < n and 0 <= y < n):  # 술래의 탐색 범위가 경계를 벗어날 경우
            continue
        if graph[x][y] == -1:  # 나무가 있는 위치라면 -> 잡을 수 없음
            continue

        for i in range(len(hider)):
            one_hider = hider[i]

            one_hider_x = one_hider[0]
            one_hider_y = one_hider[1]
            one_hider_alive = one_hider[3]

            if (x, y) == (one_hider_x, one_hider_y) and one_hider_alive == 1:
                cnt += 1
                one_hider_alive = 0
                hider[i] = [one_hider_x, one_hider_y, one_hider[2], one_hider_alive]

    return cnt


def getSeekSeq():
    global seek_seq, seek_map, seek_seq_len, nm
    d = 0
    nm = 105
    seek_seq = [0] * nm * nm * 2
    seek_map = [[0] * n for _ in range(n)]
    num = n * n - 1
    x, y = 0, 0
    seek_map[x][y] = num

    while num > 0:

        num -= 1
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0 <= nx < n and 0 <= ny < n) or seek_map[nx][ny] != 0:
            d = (d + 1) % 4

        nx = x + dx[d]
        ny = y + dy[d]

        seek_map[nx][ny] = num

        x, y = nx, ny

    seek_seq_len = n * n * 2 - 2
    for i in range(n):
        for j in range(n):
            ord = seek_map[i][j]
            seek_seq[ord] = (i, j)

            ord = seek_seq_len - ord
            seek_seq[ord] = (i, j)

    print("seek_seq : ", seek_seq)


def solve():
    total = 0
    getSeekSeq()
    for tmpK in range(1, k + 1):
        moveHider()
        moveSeek()
        score = catchHider()
        total += score * tmpK

    return total


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m, h, k = map(int, input().split())
graph = [[0] * n for _ in range(n)]

hider = []
for _ in range(m):
    # 좌표는 1 부터 시작
    x, y, d = map(int, input().split())
    if d == 2:
        d = 0
    hider.append([x - 1, y - 1, d, 1])

tree = []
for _ in range(h):
    x, y = map(int, input().split())
    tree.append([x - 1, y - 1])
    graph[x - 1][y - 1] = -1

seeker = [n // 2, n // 2, 0]

ans = solve()
print(ans)
