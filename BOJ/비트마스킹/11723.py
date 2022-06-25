# 집합

import sys
input = sys.stdin.readline
m = int(input())
bit = 0
for _ in range(m):
    s = input().split()
    if len(s) > 1:
        cal, num = s[0], int(s[1]) - 1  # num 은 인덱스
        if cal == "add":
            bit |= 1 << num
        elif cal == "remove":
            bit &= ~(1 << num)
        elif cal == "check":
            if bit & (1 << num) == 0:
                print(0)
            else:
                print(1)
        else:  # "toggle"
            bit ^= 1 << num
    else:
        if s[0] == "all":ß
            bit |= ~(0)
        else:  # "empty"
            bit &= 0
