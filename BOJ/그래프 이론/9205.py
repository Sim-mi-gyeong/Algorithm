# 맥주 마시면서 걸어가기

import sys

input = sys.stdin.readline
num = 20
dis = 50

t = int(input())
for _ in range(t):
    path = []
    n = int(input())  # 편의점 개수
    startX, startY = map(int, input().split())  # 집
    path.append((startX, startY))
    for _ in range(n):
        midX, midY = map(int, input().split())  # 편의점 좌표
        path.append((midX, midY))
    endX, endY = map(int, input().split())  # 페스티벌 위치
    path.append((endX, endY))

    for i in range(len(path[:-1])):
        diff = abs((path[i + 1][0] - path[i][0]) + (path[i + 1][1] - path[i][1]))
        if num * dis >= diff:
            check = 1
        else:
            check = 0

        if check == 0:
            print("sad")
            exit(0)

    if check == 1:
        print("happy")


"""
1
2
0 0
1000 5
2000 10
3000 15

1
0
0 0
1000 0
"""
