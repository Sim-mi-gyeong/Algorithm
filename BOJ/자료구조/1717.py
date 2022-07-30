# 집합의 표현

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = dict()
for i in range(n + 1):
    parent[i] = i


def find_parent(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x], parent)
    return parent[
        x
    ]  # return find_parent(parent[x], parent) 을 할 경우, x 와 parent 를 비교랄 위한 parent[x] 갱신 X


def union(x, y):
    parentX = find_parent(x, parent)
    parentY = find_parent(y, parent)
    # 조상(부모)이 더 작은 값으로 집합 합치기 - 이때 x 의 조상 parentX 를 더 작은 조상으로 합쳐주기
    if parentX <= parentY:
        parent[parentY] = parentX
    else:
        parent[parentX] = parentY


for _ in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(a, b)
    else:
        parA = find_parent(a, parent)
        parB = find_parent(b, parent)
        if parA == parB:
            print("YES")
        else:
            print("NO")
