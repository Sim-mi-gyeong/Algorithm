# 거짓말

import sys

input = sys.stdin.readline
n, m = map(int, input().split())


def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union(a, b):
    parentA = find_parent(a, parent)
    parentB = find_parent(b, parent)

    if parentA != parentB:
        parent[parentB] = parentA


parent = [0] * (n + 1)
knowPeopleNum, *knowpeople = map(int, input().split())
for p in knowpeople:
    parent[p] = 1


def solve(partyPeopleNum, partyPeople):
    check = True
    for p in partyPeople:
        if parent[p] != 0:
            check = False

    return check


ans = 0
for _ in range(m):
    partyPeopleNum, *partyPeople = map(int, input().split())
    if solve(partyPeopleNum, partyPeople):
        ans += 1
print(ans)
