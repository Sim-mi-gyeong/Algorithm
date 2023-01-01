# 친구 네트워크

import sys

input = sys.stdin.readline
t = int(input())


def find_parent(x, parent):
    if parent[x] != x:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union(a, b):
    parentA, parentB = find_parent(a, parent), find_parent(b, parent)
    if parentA != parentB:
        parent[parentB] = parentA
        counter[parentA] += counter[parentB]

    print(counter[parentA])


for _ in range(t):
    f = int(input())
    parent = dict()
    counter = dict()
    for _ in range(f):
        a, b = input().split()
        if a not in parent:
            parent[a] = a
            counter[a] = 1
        if b not in parent:
            parent[b] = b
            counter[b] = 1

        union(a, b)
