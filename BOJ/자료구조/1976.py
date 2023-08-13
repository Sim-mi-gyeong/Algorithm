# 여행 가자
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())  # <= 200
m = int(input())  # <= 1000
parent = [i for i in range(n + 1)]


def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union(a, b):
    parentA = find_parent(a, parent)
    parentB = find_parent(b, parent)
    if parentA < parentB:
        parent[parentB] = parentA
    else:
        parent[parentA] = parentB


for i in range(1, n + 1):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            union(i, j + 1)

q = deque(list(map(int, input().split())))


def check():
    check = True
    start = q.popleft()

    while q:
        curr = q.popleft()
        parentStart = find_parent(start, parent)
        parentEnd = find_parent(curr, parent)
        start = curr
        if parentStart == parentEnd:
            continue
        else:
            check = False
            break

    return check


if check():
    print("YES")
else:
    print("NO")
