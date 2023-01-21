# 열쇠

from collections import deque
import sys

input = sys.stdin.readline


def solve():

    ans = 0

    return ans


t = int(input().rstrip())
for _ in range(t):
    h, w = map(int, input().rstrip().split())
    graph = []
    doc = dict()
    for i in range(h):
        tmp = list(input().rstrip())
        graph.append(tmp)
        smallKey = dict()
        largeKey = dict()
        for j in range(w):
            if tmp[j] == "$":  # 문서의 위치 저장
                doc[(i, j)] = 0
            elif tmp[j].isalpha() and tmp[j].islower():
                smallKey[(i, j)] = 0
            elif tmp[j] == " ":
                largeKey[(i, j)] = 0
    key = list(input().rstrip())

    ans = solve()
