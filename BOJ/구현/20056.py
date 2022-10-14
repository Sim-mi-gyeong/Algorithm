# 마법사 상어와 파이어볼
import sys

input = sys.stdin.readline
n, m, k = map(int, input().split())

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

fire_ball = dict()
for i in range(1, m + 1):
    r, c, m, s, d = map(int, input().split())
    fire_ball[(r - 1, c - 1)] = [(m, s, d)]


def move():
    new_fire_ball = dict()
    for key, val in fire_ball.items():
        x, y = key[0], key[1]
        for fire in val:
            m, s, d = fire[0], fire[1], fire[2]
            nx = (x + (dx[d] * s)) % n
            ny = (y + (dy[d] * s)) % n
            if (nx, ny) in new_fire_ball:
                new_fire_ball[(nx, ny)].append((m, s, d))
            else:
                new_fire_ball[(nx, ny)] = [(m, s, d)]

    return new_fire_ball


def merge_and_divide():
    new_fire_ball = dict()

    for key, val in fire_ball.items():
        x, y = key[0], key[1]
        if len(val) >= 2:
            total_m = 0
            total_s = 0
            cnt = 0
            dir_even = 0
            dir_odd = 0
            for fire in val:
                m, s, d = fire[0], fire[1], fire[2]
                total_m += m
                total_s += s
                cnt += 1
                if d % 2 != 0:
                    dir_odd += 1
                else:
                    dir_even += 1
            tmp_m = int((total_m) / 5)
            tmp_s = int((total_s) / cnt)

            if tmp_m == 0:
                continue

            if dir_even == cnt or dir_odd == cnt:
                new_fire_ball[(x, y)] = [
                    (tmp_m, tmp_s, 0),
                    (tmp_m, tmp_s, 2),
                    (tmp_m, tmp_s, 4),
                    (tmp_m, tmp_s, 6),
                ]
            else:
                new_fire_ball[(x, y)] = [
                    (tmp_m, tmp_s, 1),
                    (tmp_m, tmp_s, 3),
                    (tmp_m, tmp_s, 5),
                    (tmp_m, tmp_s, 7),
                ]
        else:
            new_fire_ball[key] = val

    return new_fire_ball


for _ in range(k):
    fire_ball = move()
    fire_ball = merge_and_divide()

total = 0
for key, val in fire_ball.items():
    for fire in val:
        tmp_m = fire[0]
        total += tmp_m

print(total)
