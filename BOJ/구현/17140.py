# 이차원 배열과 연산
import sys
import copy
from collections import Counter

input = sys.stdin.readline
r, c, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(3)]


def cal_r(copy_arr):
    new_arr = []
    for row in copy_arr:
        max_row_num = 0

        row_counter_dict = Counter(row)
        row_counter_dict = dict(sorted(row_counter_dict.items(), key=lambda x: (x[1], x[0])))

        tmp_arr = []
        for key, val in row_counter_dict.items():
            tmp_arr.append(key)
            tmp_arr.append(val)

        if max_row_num < len(tmp_arr):
            max_row_num = len(tmp_arr)

        new_arr.append(tmp_arr)

    return new_arr


def cal_c(copy_arr):
    new_arr = []
    for row_idx in range(len(copy_arr)):
        col = copy_arr[row_idx][:]

        col_counter_dict = Counter(col)
        col_counter_dict = dict(sorted(col_counter_dict.items(), key=lambda x: (x[1], x[0])))

        tmp_arr = []
        for key, val in col_counter_dict.items():
            tmp_arr.append(key)
            tmp_arr.append(val)

        new_arr.append(tmp_arr)

    return new_arr


def check():
    if arr[r - 1][c - 1] == k:
        return True
    return False


time = 0


def cal():
    global arr

    row_num = len(arr)
    col_num = len(arr[0])
    copy_arr = copy.deepcopy(arr)

    if row_num >= col_num:
        arr = cal_r(copy_arr)
    else:
        arr = cal_c(copy_arr)


while True:
    if time > 100:
        print(-1)
        break
    if check():
        print(time)
        break

    cal()
    time += 1
