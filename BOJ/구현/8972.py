# 미친 아두이노
import sys

input = sys.stdin.readline

dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]
graph = []
r, c = map(int, input().split())
arduino = dict()
for i in range(r):
    tmp = list(input())
    graph.append(tmp)
    for j in range(len(tmp)):
        if tmp[j] == "I":
            startX, startY = i, j
        elif tmp[j] == "R":
            arduino[(i, j)] = 1

dir = list(map(int, input().strip()))
end_play = False
cnt = 0


def play():
    global x, y, end_play, cnt, arduino
    x, y = startX, startY
    for d in dir:
        nx = x + dx[d]
        ny = y + dy[d]
        if not (0 <= nx < r and 0 <= ny < c):
            continue
        cnt += 1
        if (nx, ny) in arduino:
            end_play = True
            return
        x, y = nx, ny

        arduino_loc = dict()
        next_arduino_loc = dict()

        for key in arduino:
            ard_x, ard_y = key[0], key[1]
            minDist = 1e9
            min_ard_nx, min_ard_ny = ard_x, ard_y
            for i in range(1, len(dx)):
                if i == 5:
                    continue
                ard_nx = ard_x + dx[i]
                ard_ny = ard_y + dy[i]
                if not (0 <= ard_nx < r and 0 <= ard_ny < c):
                    continue
                tmp_dist = abs(x - ard_nx) + abs(y - ard_ny)

                if tmp_dist < minDist:
                    minDist = tmp_dist
                    min_ard_nx, min_ard_ny = ard_nx, ard_ny

            next_ard_nx, next_ard_ny = min_ard_nx, min_ard_ny

            if (next_ard_nx, next_ard_ny) == (x, y):
                end_play = True
                return

            next_arduino_loc[(next_ard_nx, next_ard_ny)] = (
                next_arduino_loc.get((next_ard_nx, next_ard_ny), 0) + 1
            )
        for k, v in next_arduino_loc.items():
            if v >= 2:
                continue
            arduino_loc[k] = 1

        arduino = arduino_loc


play()

if end_play:
    print("kraj " + str(cnt))
else:
    result = [["."] * c for _ in range(r)]
    result[x][y] = "I"
    for i, j in arduino.keys():
        result[i][j] = "R"
    for i in range(r):
        print("".join(result[i]))
