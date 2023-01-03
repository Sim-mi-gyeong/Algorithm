# 거짓말

import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


def find_parent(x, parent):
    if x != parent[x]:
        parent[x] = find_parent(parent[x], parent)
    return parent[x]


def union(a, b):
    parentA = find_parent(a, parent)
    parentB = find_parent(b, parent)
    if parentA in knowpeople and parentB in knowpeople:
        return
    elif parentA in knowpeople:
        parent[parentB] = parentA
    elif parentB in knowpeople:
        parent[parentA] = parentB
    else:
        if parentA < parentB:
            parent[parentB] = parentA
        else:
            parent[parentA] = parentB


knowPeopleNum, *knowpeople = map(int, input().split())


def solve(partyPeopleNum, partyPeople):
    q = deque(partyPeople)
    start = q.popleft()
    while q:
        p = q.popleft()
        union(start, p)
        start = p


party = []
for _ in range(m):
    partyPeopleNum, *partyPeople = map(int, input().split())
    party.append(partyPeople)
    solve(partyPeopleNum, partyPeople)


def checkEnable():
    global ans
    for tmpPatry in party:
        check = True
        for person in tmpPatry:
            if find_parent(person, parent) in knowpeople:
                check = False
        if check:
            ans += 1


ans = 0
checkEnable()
print(ans)
