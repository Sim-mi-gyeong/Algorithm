# 병든 나이트
# dx = [2, 1, -1, -2]
# dy = [1, 2, 2, 1]
# dx = [2, -2, 1, -1]
# dy = [1, 1, 2, 2]
dx = [-2, 2, 1, -1]
dy = [1, 1, 2, 2]
cnt = 0
n, m = map(int, input().split())
x, y = n-1, 0
while (True):
    if m < sum(dy):
        for i in range(2):
            # if 0 <= x < n and 0 <= y < m: break
            if 0 > x or x >= n and 0 > y or y >= m: break
            nx = x + dx[i]
            ny = y + dy[i]
            cnt += 1
            x, y = nx, ny
            print('위치 : ', (x, y))

    else:
        for i in range(len(dx)):
            if 0 > x or x >= n and 0 > y or y >= m: break
            nx = x + dx[i]
            ny = y + dy[i]
            cnt += 1
            x, y = nx, ny
            print('위치 : ', (x, y))
        dx, dy = dx[:2], dy[:2]
    # x, y = nx, ny
print(cnt)