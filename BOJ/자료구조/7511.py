# 소셜 네트워킹 어플리케이션


import sys

input = sys.stdin.readline


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


t = int(input())
ans = []
for tc in range(1, t + 1):
    ans.append("Scenario {}:\n".format(tc))
    n = int(input())
    parent = [0] * n
    for i in range(n):
        parent[i] = i

    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        union(a, b)

    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        parentU = find_parent(u, parent)
        parentV = find_parent(v, parent)
        if parentU == parentV:
            ans.append("1\n")
        else:
            ans.append("0\n")
    ans.append("\n")
print("".join(ans))
