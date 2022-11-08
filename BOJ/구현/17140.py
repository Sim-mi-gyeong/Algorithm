# 이차원 배열과 연산
import sys

input = sys.stdin.readline
r, c, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]


def cal_r(arr):
    new_arr = []
    max_row_num = 0
    for row in arr:
        tmp_arr = []
        set_row = set(row)
        for tmp_set_row in set_row:
            if tmp_set_row == 0:
                continue
            tmp_set_row_cnt = row.count(tmp_set_row)
            tmp_arr.append((tmp_set_row, tmp_set_row_cnt))

        tmp_arr = sorted(tmp_arr, key=lambda x: (x[1], x[0]))
        new_tmp_arr = []
        for num, cnt in tmp_arr:
            new_tmp_arr.append(num)
            new_tmp_arr.append(cnt)

        max_row_num = max(max_row_num, len(new_tmp_arr))

        new_arr.append(new_tmp_arr)

    for row in new_arr:
        if len(row) > 100:
            row = row[:100]
            continue
        if len(row) < max_row_num:
            row += [0] * (max_row_num - len(row))

    return new_arr


def cal_c(arr):
    arr = list(zip(*arr))
    new_arr = []
    max_row_num = 0
    for row in arr:
        tmp_arr = []
        set_row = set(row)
        for tmp_set_row in set_row:
            if tmp_set_row == 0:
                continue
            tmp_set_row_cnt = row.count(tmp_set_row)
            tmp_arr.append((tmp_set_row, tmp_set_row_cnt))

        tmp_arr = sorted(tmp_arr, key=lambda x: (x[1], x[0]))
        new_tmp_arr = []
        for num, cnt in tmp_arr:
            new_tmp_arr.append(num)
            new_tmp_arr.append(cnt)

        max_row_num = max(max_row_num, len(new_tmp_arr))

        new_arr.append(new_tmp_arr)

    for row in new_arr:
        if len(row) > 100:
            row = row[:100]
            continue
        if len(row) < max_row_num:
            row += [0] * (max_row_num - len(row))

    new_arr = list(zip(*new_arr))

    return new_arr


def check(arr):
    if len(arr) < r or len(arr[0]) < c:
        return False
    if arr[r - 1][c - 1] == k:
        return True
    return False


def cal():
    global arr
    row_num = len(arr)
    col_num = len(arr[0])

    if row_num >= col_num:
        arr = cal_r(arr)
    else:
        arr = cal_c(arr)


time = 0
while True:
    if time > 100:
        print(-1)
        break

    if check(arr):
        print(time)
        break

    cal()
    time += 1
