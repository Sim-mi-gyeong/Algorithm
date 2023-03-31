import sys

input = sys.stdin.readline
n, k = map(int, input().rstrip().split())


def move(curr, target, size):
    moved = 0
    if curr < target:
        moved += target - curr
    elif curr > target:
        moved += (size - curr) + target
    return moved


def rotate_table(idx):
    tmpCnt = 0

    x, currX, currY, targetX, targetY = data[idx]

    moveX = move(currX, targetX, n)
    moveY = move(currY, targetY, n)
    tmpCnt = moveX + moveY

    for d2 in range(idx + 1, k):
        if data[d2][0] == x:
            data[d2][1] = targetX
            data[d2][2] = targetY
        else:
            if data[d2][1] == currX:
                data[d2][2] += moveY
                if data[d2][2] >= n:
                    data[d2][2] %= n
            if data[d2][2] == targetY:
                data[d2][1] += moveX
                if data[d2][1] >= n:
                    data[d2][1] %= n

    return tmpCnt


data = []
for _ in range(k):
    x, r, c = map(int, input().rstrip().split())
    data.append([x, (x - 1) // n, (x - 1) % n, r - 1, c - 1])

for i in range(k):
    cnt = rotate_table(i)
    print(cnt)
